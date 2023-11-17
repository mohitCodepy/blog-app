from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views import View
from .models import Blog, Comment
from .forms import BlogPostForm, CommentForm


class BlogListView(View):
    template_name = 'blog/post_list.html'

    def get(self, request):
        blogs = Blog.objects.all().order_by('-publication_date')
        paginator = Paginator(blogs, 10)  # Show 10 blogs per page

        page = request.GET.get('page')
        blogs = paginator.get_page(page)

        return render(request, self.template_name, {'blogs': blogs})


class BlogDetailView(View):
    template_name = 'blog/post_detail.html'

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        comments = Comment.objects.filter(blog=blog)
        comment_form = CommentForm()

        return render(request, self.template_name, {'blog': blog, 'comments': comments, 'comment_form': comment_form})


class BlogCreateView(View):
    template_name = 'blog/post_create.html'
    form_class = BlogPostForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author.user = request.user
            blog.save()
            return redirect('post_detail', pk=blog.pk)
        return render(request, self.template_name, {'form': form})


class BlogUpdateView(View):
    template_name = 'blog/post_edit.html'
    form_class = BlogPostForm

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        form = self.form_class(instance=blog)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        form = self.form_class(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('post_detail', pk=blog.pk)
        return render(request, self.template_name, {'form': form})


class BlogDeleteView(View):
    template_name = 'blog/post_confirm_delete.html'

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        return render(request, self.template_name, {'blog': blog})

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return redirect('post_list')


class CommentCreateView(View):
    form_class = CommentForm

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
        return redirect('post_detail', pk=pk)

