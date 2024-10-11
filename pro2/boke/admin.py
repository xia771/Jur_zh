from django.contrib import admin

from boke.models import Post, Comment
from boke.views import post_list, post_detail, add_comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

