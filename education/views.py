from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Subject , Course , Module , Text , Video , Image , File , Topic , Comment , Students , LatestNews  
from django.views.generic.list import ListView
from django.db.models import Count
from django.views.generic.detail import DetailView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CommentForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView
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
        context['students'] = Students.objects.all()
        context['news'] = LatestNews.objects.all()
        context['courses'] = Course.objects.annotate(student_count=Count('student'))
        return context


class CourseView(TemplateView):
    template_name = 'education/course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        context['subjects'] = Subject.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'education/about.html'
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["students"] = Students.objects.all()
        return context
    

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


class SubjectCourseListView(ListView):
    model = Course
    template_name = 'education/subject_courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.filter(subject__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject'] = Subject.objects.get(slug=self.kwargs['slug'])
        return context





class CourseDetailView( DetailView):
    model = Course
    template_name = 'education/course_detail.html'
    context_object_name = 'course'




class CourseViewDetail(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'education/course_view_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        context['topics'] = Topic.objects.filter(module__course=self.object)
        context['modules'] = course.modules.prefetch_related('topics__content_type')
        return context
