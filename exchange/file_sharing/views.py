from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import LoginUserForm
from .models import Record, Discipline
from django.views.generic import ListView, DetailView, FormView
from .utils import *


class RecordHome(DataMixin, ListView):
    model = Record
    template_name = 'file_sharing/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получение уже сформированного контекста для шаблона

        c_def = self.get_user_context(title='Главная страница')
        # объединение двух словарей
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Record.objects.filter(group=user.group).select_related('discipline')  # сжатый запрос (оптимизация сайта)


def about(request):
    return render(request, 'file_sharing/about.html', {'menu': menu, 'title': 'О сайте'})


# def addpage(request):
#     return HttpResponse('addpage')


def contact(request):
    return render(request, 'file_sharing/contact.html', {'menu': menu, 'title': 'Контакты'})


class ShowPost(DataMixin, DetailView):
    model = Record
    template_name = 'file_sharing/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получение уже сформированного контекста для шаблона
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class RecordDiscipline(DataMixin, ListView):
    model = Record
    template_name = 'file_sharing/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Record.objects.filter(discipline__slug=self.kwargs['discipline_slug']).select_related(
            'discipline')  # сжатый запрос (оптимизация сайта)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получение уже сформированного контекста для шаблона
        d = Discipline.objects.get(slug=self.kwargs['discipline_slug'])
        c_def = self.get_user_context(title='Дисциплина - ' + str(d.name),
                                      discipline_selected=d.pk)
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm  # Форма из forms.py
    template_name = 'file_sharing/login.html'  # templates

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()

        group = Group.objects.filter(number=user).first()
        if group is not None:
            return super().form_valid(form)
        else:
            messages.error(self.request, "Группы с вашим именем не существует.")
            return self.form_invalid(form)


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

