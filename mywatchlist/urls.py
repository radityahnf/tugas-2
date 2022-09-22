# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_watchlist, xml_return, json_return, filtered_json_return, filtered_xml_return, count_movie

app_name = 'mywatchlist'

urlpatterns = [
    path('', count_movie, name='count_movie'),
    path('html/', show_watchlist, name='show_watchlist'),
    path('xml/', xml_return, name='xml_return'), 
    path('json/', json_return, name='json_return'), 
    path('json/<int:id>', filtered_json_return, name='filtered_json_return'),
    path('xml/<int:id>', filtered_xml_return, name='filtered_xml_return'),
]