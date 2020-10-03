from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Information


class InformationListView(ListView):
    model = Information
    template_name = 'base.html'
