from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import TopicViewSet , CommentViewSet



from .views import (
    IndexView, CourseView, AboutView, TeacherView,
    SubjectCourseListView, CourseDetailView, CourseViewDetail
)

from .api_views import (
    SubjectListView, 
  CourseCreateView , AllMethodsCourseView
   
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

  

    # ==== API: Courses ====
      path('api/courses/<int:pk>', AllMethodsCourseView.as_view(), name='api-subject-delete'),
      path('api/courses/create/', CourseCreateView.as_view(), name='api-course-create'),

]

router = DefaultRouter()
router.register(r'topics', TopicViewSet, basename='topic')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls

