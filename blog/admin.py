from django.contrib import admin
from .models import Post

# Use admin file to define interactions with models

# To make Post model visible to admin must register
admin.site.register(Post)
