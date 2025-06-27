from django.db import models
from django.conf import settings  
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.views.generic import ListView


class Subject(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='subject/images' , null=True, blank=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField(null=True, blank=True)
    duration = models.TimeField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_courses',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to='course/images')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class ItemBase(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Text(ItemBase):
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Video(ItemBase):
    url = models.URLField()

    def __str__(self):
        return f'{self.title} - {self.pk}'


class Image(ItemBase):
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class File(ItemBase):
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title


class Topic(models.Model):
    module = models.ForeignKey(Module, related_name='topics', on_delete=models.CASCADE)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('text', 'video', 'image', 'file')}
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    my_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['my_order']
    def __str__(self):
        return f"{self.module.title} - {self.content_type} - {self.item}"





class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    topic = models.ForeignKey(
        Topic,
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Students(models.Model):
    name = models.CharField(max_length=255)
    students_opinion = models.TextField(null=True, blank=True)
    students_image = models.ImageField(upload_to='student/images')
    course = models.ForeignKey(Course, related_name='student', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.name


class LatestNews(models.Model):
    image = models.ImageField(upload_to='news/images')
    title = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


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

