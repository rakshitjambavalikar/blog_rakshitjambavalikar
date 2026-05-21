from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import BlogPost,Comment
# Create your views here.
#homepate view
def home(request):

    posts = BlogPost.objects.order_by('-created_at') 

    context = {

        'posts': posts

    }

    return render(request, 'blog/home.html', context)

#post detail view
# post detail view
def post_detail(request, post_id):

    # Get the blog post by ID
    post = get_object_or_404(
        BlogPost,
        id=post_id
    )

    # Fetch all comments linked to this post
    comments = Comment.objects.filter(post=post)

    # Data sent to template
    context = {

        'post': post,
        'comments': comments

    }

    return render(
        request,
        'blog/post_detail.html',
        context
    )