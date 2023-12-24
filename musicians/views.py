from django.shortcuts import render, redirect
from .forms import AddMusiciansForms
from .models import Musician
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.utils.decorators import method_decorator
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Logged Out Successfully')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'type': 'Register'})


class UserLogin(LoginView):
    template_name = 'register.html'
    extra_context = {'type': 'Log In'}

    def get_success_url(self) -> str:
        return reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Succesfull')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Your Information Incorrect.')
        return super().form_invalid(form)


class UserLogOut(LogoutView):
    next_page = 'homepage'


@method_decorator(login_required, name='dispatch')
class AddMusicians(CreateView):
    model = Musician
    form_class = AddMusiciansForms
    template_name = 'add_musicians.html'
    success_url = reverse_lazy('homepage')


@method_decorator(login_required, name='dispatch')
class EditMusicians(UpdateView):
    model = Musician
    form_class = AddMusiciansForms
    template_name = 'add_musicians.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'
