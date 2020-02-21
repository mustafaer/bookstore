from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Author


def index(request):
    return HttpResponse("Anasayfa")


def authors(request):
    context = {
        'authors_list': Author.objects.all()
    }
    return render(request, 'authors.html', context)


def books(request):
    return HttpResponse("Kitaplar")


def authorDetails(request, authorId):
    try:
        context = {
            'author_detail': Author.objects.get(pk=authorId)
        }
        return render(request, 'authorDetail.html', context)
    except Author.DoesNotExist:
        raise Http404("Yazar Bulunamadı")
