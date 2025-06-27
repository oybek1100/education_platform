from .views import IndexView , CourseView , AboutView , TeacherView ,  SubjectCourseListView , CourseDetailView, CourseViewDetail
from django.urls import path

app_name = 'education'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('courses/', CourseView.as_view(), name='course'),
    path('about', AboutView.as_view(), name='about'),
    path('teacher', TeacherView.as_view(), name='teacher'),
    path('subjects/<slug:slug>/', SubjectCourseListView.as_view(), name='subject_courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail') ,
    path('courses/<int:pk>/view/', CourseViewDetail.as_view(), name='course_view_detail'),
]