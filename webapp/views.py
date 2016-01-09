from django.shortcuts import get_object_or_404, render, redirect

from django.forms import modelformset_factory

from .models import Series
from .models import Round
from .models import Prediction
from .models import Nilnils

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

def prediction_new(request, s_pk, r_pk):
    round_f = get_object_or_404(Round, id=r_pk)

    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            prediction = form.save(commit=False)
            prediction.user = request.user
            prediction.round_f = round_f
            prediction.save()
            return redirect('series_detail', pk=s_pk)
    else:
        form = PredictionForm()
    return render(request, 'webapp/prediction_edit.html', {'form': form})


def manage_prediction(request, s_pk, r_pk):
    round_f = get_object_or_404(Round, id=r_pk)
    PredictionFormSet = modelformset_factory(Prediction, fields=('team', ), max_num=1)
    if request.method == "POST":
        formset = PredictionFormSet(request.POST, request.FILES,
                                queryset=Prediction.objects.filter(round_f=r_pk, user=request.user))
        if formset.is_valid():
            for form in formset:
                prediction = form.save(commit=False)
                prediction.user = request.user
                prediction.round_f = round_f
                prediction.save()
            return redirect('series_detail', pk=s_pk)
    else:
        formset = PredictionFormSet(queryset=Prediction.objects.filter(round_f=r_pk, user=request.user))
    return render(request, 'webapp/prediction_edit.html', {'formset': formset})




