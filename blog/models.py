from django.db import models

# Create your models here.

class Category(models.Model):

    # Category name visible to users
    # Example: Django
    name = models.CharField(max_length=100, unique=True)

    # URL-friendly version
    # Example: django
    slug = models.SlugField(unique=True)

    # This controls how the object appears
    # inside Django admin and shell
    def __str__(self):
        return self.name  
    
class BlogPost(models.Model):

    # Title field
    title = models.CharField(max_length=200)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts',
        null=True,
        blank=True
    )

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

      