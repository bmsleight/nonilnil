from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Series
from .models import Round
from .models import Prediction
from .models import Nilnils
# Create your views here.

def series_list(request):
    series = Series.objects.order_by('-id')
    context = {'series': series}
    return render(request, 'webapp/index.html', context)



def series_detail(request, pk):
    series = get_object_or_404(Series, id=pk)
    round_f = Round.objects.filter(series=series).order_by('-id')
    return render(request, 'webapp/detail.html', {'series': series, 'round_f': round_f})

