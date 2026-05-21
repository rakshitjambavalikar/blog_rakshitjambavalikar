from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import BlogPost
# Create your views here.
#homepate view
def home(request):

    posts = BlogPost.objects.all() 

    context = {

        'posts': posts

    }

    return render(request, 'blog/home.html', context)

#post detail view
def post_detail(request, post_id):

    post =  post = get_object_or_404(
        BlogPost,
        id=post_id
    )

    context = {

        'post': post

    }

    return render(request, 'blog/post_detail.html', context)