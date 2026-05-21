from django.db import models

# Create your models here.
class BlogPost(models.Model):

    # Title field
    title = models.CharField(max_length=200)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        # Show title instead of "BlogPost object"
        return self.title
    
# Comment model
class Comment(models.Model):

    # Link comment to a specific blog post
    # If blog post is deleted,
    # delete related comments too
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE
    )

    # Name of comment author
    author_name = models.CharField(max_length=100)

    # Comment text
    content = models.TextField()

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)


    # Readable representation
    def __str__(self):

        return f"Comment by {self.author_name}"    