from django.db import models
from blog.mixin import CreatedUpdatedMixin

from authentication.models import UserProfile


class Blog(CreatedUpdatedMixin):
    """
    Blog
        Authors can post a blog with title and content
    """
    author = models.ForeignKey(UserProfile, related_name="author_blogs", on_delete=models.SET_DEFAULT, default='Deleted User')
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author.user.username}"


class Comment(CreatedUpdatedMixin):
    """
    Comment
        Blog can contains multiple comments by users
    """
    blog = models.ForeignKey(Blog, related_name="blog_comments", on_delete=models.CASCADE)
    commented_by = models.ForeignKey(UserProfile, related_name="user_comments", null=True, on_delete=models.SET_DEFAULT, default='Deleted User')
    commented_on = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    def __str__(self):
        return f"Comments for {self.blog.title}"


class Tag(CreatedUpdatedMixin):
    """
    Tag
        Blogs can contains multiple tags to identify the particular category
    """

    blog = models.ManyToManyField(Blog, related_name="blogs_tags")
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
