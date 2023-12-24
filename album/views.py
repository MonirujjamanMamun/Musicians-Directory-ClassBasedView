from django.shortcuts import render, redirect
from .forms import AddAlbumForms
from .models import Album
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(login_required, name='dispatch')
class AddAlbum(CreateView):
    model = Album
    form_class = AddAlbumForms
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):

        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class AlbumEdit(UpdateView):
    model = Album
    form_class = AddAlbumForms
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'


@method_decorator(login_required, name='dispatch')
class AlbumDelete(DeleteView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'delete_album.html'
    success_url = reverse_lazy('homepage')
