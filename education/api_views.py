from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subject , Course
from rest_framework.status import HTTP_200_OK , HTTP_404_NOT_FOUND , HTTP_201_CREATED , HTTP_400_BAD_REQUEST
from .serializers import SubjectSerializer , CourseSerializer


class SubjectListView(APIView):
    def get(self, request, ):
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject , many=True)
        return Response(serializer.data)  
    



class SubjectDetialView(APIView):
    def get(self , request , slug):
        try:
            subject = Subject.objects.get(slug = slug) #sluglari webDeveloping , mobileDeveloping
            serializer = SubjectSerializer(subject)
            return Response(serializer.data , status=HTTP_200_OK)
        except Subject.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

class SubjectCreateView(APIView):
    def post(self , request):
        serializer = SubjectSerializer( data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data , status=HTTP_201_CREATED)
        return Response(serializer.errors , status=HTTP_400_BAD_REQUEST)


class SubjectUpdateView(APIView):
    def put(self , request , slug):
        try:
            subject = Subject.objects.get(slug = slug)
            serializer = SubjectSerializer(subject , data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=HTTP_200_OK)
            return Response(serializer.errors , status=HTTP_400_BAD_REQUEST)
        except Subject.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

class SubjectDeleteView(APIView):
    def delete(self , request , slug):
        try:
            subject = Subject.objects.get(slug = slug)
            subject.delete()
            return Response(status=HTTP_200_OK)
        except Subject.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class CourseListView(APIView):
    def get(self , request):
        course = Course.objects.all()
        serializer = CourseSerializer(course , many=True)
        return Response(serializer.data)


class CourseDetailViewww(APIView):
    def get(self , request,slug ):
        try :
            course = Course.objects.get(slug = slug)
            serializer = CourseSerializer(course)
            return Response(serializer.data , status=HTTP_200_OK)
        except Course.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

class CourseCreateView(APIView):
    def post(self , request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=HTTP_201_CREATED)
        return Response(serializer.errors , status=HTTP_400_BAD_REQUEST)
    
class CourseUpdateView(APIView):
    def put(self  , request , slug):
        try:
            course = Course.objects.get(slug = slug)
            serializer = CourseSerializer(course , data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=HTTP_200_OK)
            return Response(serializer.errors , status=HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            return Response(serializer.errors , status=HTTP_404_NOT_FOUND)
        

class CourseDeleteView(APIView):
    def delete(self , request, slug):
        try :
            course = Course.objects.get(slug = slug)
            course.delete()
            return Response(status=HTTP_200_OK)
        except Course.DoesNotExist:
            return Response(  status=HTTP_404_NOT_FOUND)
            