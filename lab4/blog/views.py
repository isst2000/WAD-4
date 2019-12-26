from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.views import generic
from django.views.generic import FormView, View
from lab4.blog.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import datetime
from .models import *


class MainView(generic.ListView):
    template_name = 'main.html'
    context_object_name = 'main_postList'

    def get_queryset(self):
        return Post.objects.annotate(num=Count('comment')).order_by('-publication_date')[:5]


class PostView(generic.DeleteView):
    model = Post
    template_name = 'post.html'


class RegistrationForm(FormView):
    form_class = RegistrationForm
    success_url = "/login/"
    template_name = "registration.html"

    def form_valid(self, form):
        form.save()
        return super(RegistrationForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationForm, self).form_invalid(form)


class LoginForm(FormView):
    form_class = LoginForm
    success_url = "/profile/"
    template_name = "login.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginForm, self).form_valid(form)


@login_required(login_url='/login/')
def user_profile(request):
    return render(request, 'profile.html')


class LogoutForm(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
