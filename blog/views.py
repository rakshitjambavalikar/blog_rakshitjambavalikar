from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
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
# post detail view
def post_detail(request, post_id):

    # Fetch the blog post using ID
    post = get_object_or_404(
        BlogPost,
        id=post_id
    )

    # -----------------------------------
    # HANDLE COMMENT FORM SUBMISSION
    # -----------------------------------

    # Check if form was submitted
    if request.method == 'POST':

        # Get data from submitted form
        author_name = request.POST.get('author_name')

        content = request.POST.get('content')

        # Create new comment object in database
        Comment.objects.create(

            post=post,
            author_name=author_name,
            content=content

        )

        # Redirect back to same post page
        return redirect(
        'post_detail',
        post_id=post.id
)

    # Fetch comments related to this post
    comments = Comment.objects.filter(
        post=post
    )

    # Send data to template
    context = {

        'post': post,
        'comments': comments

    }

    return render(
        request,
        'blog/post_detail.html',
        context
    )

# Contact page view
def contact(request):

    # Render contact template
    return render(
        request,
        'blog/contact.html'
    )