from django.contrib import admin
from .models import User, Post, Comment, Staff, Request, Application

# Register your models here.
admin.site.register(User),
admin.site.register(Post),
admin.site.register(Comment),
admin.site.register(Staff),
admin.site.register(Request),
admin.site.register(Application),