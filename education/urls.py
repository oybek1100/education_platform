from .views import IndexView , CourseView , AboutView , TeacherView
from django.urls import path

app_name = 'education'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('courses/', CourseView.as_view(), name='course'),
    path('about', AboutView.as_view(), name='about'),
    path('teacher', TeacherView.as_view(), name='teacher'),
]