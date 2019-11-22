from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, post_comment_view, update_post_comment_view, PostCommentDeleteView
from . import views

"""Urls for the blogs section of the site. These urls will be added to the '/blog' extension set up within the main site urls file in the 'cadwork' folder"""
# <str:username> and <int:pk> extensions to specify the url extension depending on the specific post or user who created the post.
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', views.post_comment_view, name='post-comment-create'),
    path('post/<int:pk>/comment/update/', views.update_post_comment_view, name='post-comment-update'),
    path('post/<int:pk>/comment/delete', PostCommentDeleteView.as_view(), name='post-comment-delete')
]