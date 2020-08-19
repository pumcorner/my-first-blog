from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def _str_(self):
        return self.title

class Personal_info(models.Model):

    title = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='upload/',default='upload/resume_silin.jpeg')
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    my_words = models.TextField()
    changed_date = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(default=timezone.now)

    # class Contact:
    #     mobile = models.CharField(max_length=50)
    #     email = models.CharField(max_length=50)
    #     app = models.CharField(max_length=50)

    def photo_url(self):
        if self.pic and hasattr(self.pic,'url'):
            return self.pic.url
        else:
            return 'upload/resume_silin.jpeg'

    def published(self):
        self.changed_date = timezone.now()
        self.save()

    def _str_(self):
        return self.title

class Work_detail(models.Model):

    title = models.CharField(max_length = 50)
    duration = models.CharField(max_length=10)
    details = models.TextField()

    def _srt_(self):
        return self.title

class Comment(models.Model):
    #link comment to model Post
    #use relate name to have access in post model
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()


    def __str__(self):
        return self.text

class Guest_post(models.Model):
    #This is the guest anonymous post
    #Has no connection with user but is deleteable and approvable by log-in user
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()
