from django.urls import path

from blog.views import BlogCreateView, BlogListView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path('create/', BlogCreateView.as_view()),
    path('list/', BlogListView.as_view()),
    path('update/<int:pk>', BlogUpdateView.as_view()),
    path('delete/<int:pk>', BlogDeleteView.as_view()),
]