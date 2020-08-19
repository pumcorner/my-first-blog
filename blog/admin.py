from django.contrib import admin
from .models import Post
from .models import Personal_info
from .models import Work_detail
from .models import Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Personal_info)
admin.site.register(Work_detail)
admin.site.register(Comment)
