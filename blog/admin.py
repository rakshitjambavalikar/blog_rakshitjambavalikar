from django.contrib import admin

# Register your models here.
# Import Django admin system
from django.contrib import admin

# Import BlogPost model
from .models import BlogPost, Comment


# Register BlogPost model in admin panel
admin.site.register(BlogPost)
admin.site.register(Comment)