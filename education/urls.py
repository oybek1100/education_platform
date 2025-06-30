from django.urls import path, include
from .views import (
    IndexView, CourseView, AboutView, TeacherView,
    SubjectCourseListView, CourseDetailView, CourseViewDetail
)

from .api_views import (
    SubjectListView, SubjectDetialView, SubjectCreateView,
    SubjectUpdateView, SubjectDeleteView,
    CourseListView, CourseDetailViewww, CourseCreateView,
    CourseUpdateView, CourseDeleteView
)

app_name = 'education'

urlpatterns = [
    # ==== Frontend Views ====
    path('', IndexView.as_view(), name='index'),
    path('courses/', CourseView.as_view(), name='course'),
    path('about/', AboutView.as_view(), name='about'),
    path('teacher/', TeacherView.as_view(), name='teacher'),
    path('subjects/<slug:slug>/', SubjectCourseListView.as_view(), name='subject_courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/<int:pk>/view/', CourseViewDetail.as_view(), name='course_view_detail'),

    # ==== DRF Auth Login ====
    path('api-auth/', include('rest_framework.urls')),

    # ==== API: Subjects ====
    path('api/subjects/', SubjectListView.as_view(), name='api-subject-list'),
    path('api/subjects/create/', SubjectCreateView.as_view(), name='api-subject-create'),
    path('api/subjects/<slug:slug>/', SubjectDetialView.as_view(), name='api-subject-detail'),
    path('api/subjects/<slug:slug>/update/', SubjectUpdateView.as_view(), name='api-subject-update'),
    path('api/subjects/<slug:slug>/delete/', SubjectDeleteView.as_view(), name='api-subject-delete'),

    # ==== API: Courses ====
    path('api/courses/', CourseListView.as_view(), name='api-course-list'),
    path('api/courses/create/', CourseCreateView.as_view(), name='api-course-create'),
    path('api/courses/<int:pk>/', CourseDetailViewww.as_view(), name='api-course-detail'),
    path('api/courses/<int:pk>/update/', CourseUpdateView.as_view(), name='api-course-update'),
    path('api/courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='api-course-delete'),
]
