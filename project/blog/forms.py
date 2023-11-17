from django import forms
from .models import Blog, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author']

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        if author != self.instance.author:
            raise forms.ValidationError("You are not allowed to edit this post.")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
