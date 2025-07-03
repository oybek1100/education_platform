from rest_framework import serializers
from .models import Subject , Course , Topic , Comment



class CourseSerializer(serializers.ModelSerializer):

    subject_title = serializers.StringRelatedField(source='subject.title' , read_only=True)

    owner = serializers.SerializerMethodField()

    def get_owner(self , obj):
        if obj.owner:
            return obj.owner.username
        return None
    
    class Meta:
        model = Course
        fields = '__all__'
    

class SubjectSerializer(serializers.ModelSerializer):

    full_image_url = serializers.SerializerMethodField()

    course_count = serializers.SerializerMethodField()

    def get_course_count(self , obj):
        return obj.courses.count()
    def get_full_image_url(self , obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url )
        return None
    class Meta:
        model = Subject
        fields = '__all__'

        
class TopicSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



