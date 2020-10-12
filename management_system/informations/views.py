from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Information


class InformationCreateView(generic.CreateView):
    model = Information
    template_name = 'add_informations.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('add_informations')

    def form_valid(self, form):
        form.instance.author = self.request.user
        super().form_valid(form)
        return redirect('add_informations')


class InformationListView(generic.ListView):
    model = Information
    context_object_name = 'informations'
    paginate_by = 2
    template_name = 'informations.html'


class InformationDetailView(generic.DetailView):
    model = Information
    context_object_name = 'information'
    template_name = 'detail_information.html'
