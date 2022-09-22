from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_watchlist(req):
    data_watchlist = MyWatchList.objects.all()
    ctx = {
        'watchlist':  data_watchlist,
        'nama': 'Muhammad Raditya Hanif',
        'id': '2106750585'
    }

    return render(req, "watchlist.html", ctx)

def xml_return(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def json_return(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def filtered_json_return(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def filtered_xml_return(request,id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def count_movie(request):
    movies = MyWatchList.objects.all()
    is_watched = 0
    watched_more = False
    
    
    for item in movies:
        if item.watched:
            is_watched += 1
    
    if is_watched > (MyWatchList.objects.count())/2:
        watched_more = True
        
   
    context = {
        'watched_more' : watched_more,
        'nama': 'Muhammad Raditya Hanif',
        'id': '2106750585'
    }

    return render(request, "main.html", context)