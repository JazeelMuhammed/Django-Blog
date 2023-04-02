from django.db import models
from django.utils import timezone
# Since we need an author for each BlogPost and this will be the user who created the Post.
from django.contrib.auth.models import User
# FOR REVERSING THE URL AFTER CREATING A "BLOG"
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Since 1 user can have multiple BlogPosts, but One BlogPost must have only One user. ie; One-to-Many Relationship.
    # So we must specify author in foreign key, author here is the "User" in the admin page.
    # CASCADE means that "When the User is deleted, Also deletes his "BlogPosts".
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # auto_now_add enables to catch the date when this object is 1st created. so we doesn't use that, instead we use default
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # like {% url 'blog-details' post.pk %} in "home.html"
        return reverse('blog-details', kwargs={'pk': self.pk})


