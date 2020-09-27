from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import t1

def movies(request):
    ###  从models取数据传给template  ###
    #n = t1.objects.all()
    #queryset = t1.objects.values('n_star')
    #condtions = {'n_star__gt': 3}
    #n = queryset.filter(**condtions).all()
    n = t1.objects.exclude(n_star__lt=3).all()
    return render(request, 'movies.html', locals())