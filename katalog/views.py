from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(req):
    data_katalog = CatalogItem.objects.all()
    ctx = {
        'list_katalog':  data_katalog,
        'nama': 'Muhammad Raditya Hanif',
        'id': '2106750585'

    }

    return render(req, "katalog.html", ctx)