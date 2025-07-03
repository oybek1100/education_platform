from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subject , Course , Topic , Comment
from rest_framework.status import HTTP_200_OK , HTTP_404_NOT_FOUND , HTTP_201_CREATED , HTTP_400_BAD_REQUEST
from .serializers import SubjectSerializer , CourseSerializer , TopicSerializer , CommentSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import permissions , viewsets
from django.db.models import Avg


class SubjectListView(ListCreateAPIView):
 
    serializer_class = SubjectSerializer
    def get_queryset(self):
        return Subject.objects.all().order_by('-id')
   
# class SubjectListView(APIView):
#     def get(self , request):
#         subject = Subject.objects.all()
#         serializer = SubjectSerializer(subject , many=True , context = {'request': request})
#         return Response(serializer.data , status=HTTP_200_OK)





class CourseCreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AllMethodsCourseView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


#Menda comment topicga ulangan ekan shunga topicni yozyabman

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().annotate(avg_rating=Avg('comments__rating'))
    serializer_class = TopicSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
            