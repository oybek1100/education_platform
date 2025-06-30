from rest_framework import serializers
from .models import Subject , Course

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [ 'slug' , 'title' ]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [   'title' , 'overview' ]
    
