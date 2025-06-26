from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Subject , Course , Module , Text , Video , Image , File , Topic , Comment

class BaseView(TemplateView):
    template_name = 'education/base.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context


class IndexView(TemplateView):
    template_name = 'education/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context

class CourseView(TemplateView):
    template_name = 'education/course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'education/about.html'

class TeacherView(TemplateView):
    template_name = 'education/teacher.html'
    from django.views.generic import TemplateView

class TeacherView(TemplateView):
    template_name = 'education/teacher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = [
            {"img": "1", "name": "Oysha Boriyeva", "title": "Python Backend"},
            {"img": "2", "name": "Qozi Qochqorov", "title": "React JS Frontend"},
            {"img": "3", "name": "Matluba Teshayeva", "title": "Flutter"},
            {"img": "4", "name": "Ali Valiyev", "title": "React Native"},
        ]
        return context

