from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import New
from .forms import ContactMessageForm

# Create your views here.


def home_page_view(request):
    return render(request, 'news/index.html')


def category_page_view(request):
    return render(request, 'news/category.html')


def single_page_view(request):
    return render(request, 'news/single.html')


def contact_page_view(request):
    form = ContactMessageForm(request.POST or None)
    context = {
        'form': form
    }
    if request.POST and form.is_valid():
        form.save()
        return render(request, 'news/contact.html', context)
    return render(request, 'news/contact.html', context)
