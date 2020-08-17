from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

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
