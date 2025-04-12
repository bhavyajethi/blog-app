from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    # This looks for blog/post_list.html meaning <app>/<model>_<view_type>.html
    path('', PostListView.as_view(), name='blog-home'),
    path('_post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('_post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('_post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
