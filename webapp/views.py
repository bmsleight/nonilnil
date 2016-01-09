from django.shortcuts import get_object_or_404, render, redirect

from django.forms import modelformset_factory
from django.utils import timezone

from .models import Series
from .models import Round
from .models import Prediction
from .models import Nilnils

from django.contrib.auth.decorators import login_required

from .forms import PredictionForm

# Create your views here.

def series_list(request):
    series = Series.objects.order_by('-id')
    context = {'series': series}
    return render(request, 'webapp/index.html', context)

def series_detail(request, pk):
    series = get_object_or_404(Series, id=pk)
    round_f = Round.objects.filter(series=series).order_by('-id')
    return render(request, 'webapp/detail.html', {'series': series, 'round_f': round_f})

def loser_detail(request, pk):
    series = get_object_or_404(Series, id=pk)
    round_f = Round.objects.filter(series=series).order_by('-id')
    return render(request, 'webapp/detail.html', {'series': series, 'round_f': round_f, 'loser': True})

@login_required
def manage_nilnils(request, s_pk, r_pk):
    round_f = get_object_or_404(Round, id=r_pk)
    predictions_all_users = Prediction.objects.filter(round_f=round_f)
    total_team = len( Prediction.objects.filter(round_f=round_f).values('team'))
    print(predictions_all_users, Prediction.objects.filter(round_f=round_f).values('team') )
    NilnilsFormSet = modelformset_factory(Nilnils, fields=('team', 'ohno'), max_num=total_team)
    if request.method == 'POST':
        formset = NilnilsFormSet(request.POST, request.FILES, queryset=Nilnils.objects.filter(round_f=r_pk))
        if formset.is_valid():
            formset.save()
    else:
        formset = NilnilsFormSet(queryset=Nilnils.objects.filter(round_f=r_pk))
    return render(request, 'webapp/nilnil_edit.html', {'formset': formset, 'all_predictions': predictions_all_users, 'round_f': round_f})

@login_required
def manage_prediction(request, s_pk, r_pk):
    round_f = get_object_or_404(Round, id=r_pk)
    PredictionFormSet = modelformset_factory(Prediction, fields=('team', ), max_num=1)
    message = ""
    all_rounds = Round.objects.filter(series=round_f.series.id)
    all_predictions = Prediction.objects.filter(round_f=all_rounds, user=request.user)
    for prediction in all_predictions:
       if prediction.failed():
           return redirect('loser_detail', pk=s_pk)

    if request.method == "POST":
        formset = PredictionFormSet(request.POST, request.FILES,
                                queryset=Prediction.objects.filter(round_f=r_pk, user=request.user))
        if timezone.now() > round_f.round_date :
             message = "Too late for to make or change your prediction. "
#            return redirect('series_detail', pk=s_pk)
        if formset.is_valid():
            for form in formset:
                prediction = form.save(commit=False)
                try:
                    team_count = Prediction.objects.filter(round_f=all_rounds, team=prediction.team, user=request.user).count()
                    if team_count >0:
                        message += "You have already used " + str(prediction.team) + " in this series (or just re-saving your team)"
                except:
                    pass

        if formset.is_valid() and message == "":
            for form in formset:
                if form.is_valid():
                    prediction = form.save(commit=False)
                    prediction.user = request.user
                    prediction.round_f = round_f
                    try:
                        prediction.save()
                    except:
                        pass
            return redirect('series_detail', pk=s_pk)
    else:
        formset = PredictionFormSet(queryset=Prediction.objects.filter(round_f=r_pk, user=request.user))
    return render(request, 'webapp/prediction_edit.html', {'formset': formset, 'round_f': round_f, 'message': message, 'all_predictions': all_predictions})




