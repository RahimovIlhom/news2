from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import New

# Create your views here.


def news_list(request):
    template = loader.get_template('news/news_list.html')
    news = New.published.all()  # news = New.objects.all()
    context = {
        'news': news,
    }
    return HttpResponse(template.render(context, request))
