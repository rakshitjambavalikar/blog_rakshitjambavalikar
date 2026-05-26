# Import path function for URL routing
from django.urls import path

# Import views from current app
from . import views


# URL patterns list
urlpatterns = [

    path('', views.home, name='home'),  # URL pattern for homepage

    path('post/<int:post_id>/', views.post_detail, name='post_detail'), 
    path('contact/',views.contact,name='contact'),
    path('category/<slug:slug>/',views.category_posts,name='category_posts'),
]