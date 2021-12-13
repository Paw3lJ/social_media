from django.urls import path
from .views import PostListView, PostDetail, PostEdit, PostDelete,CommentDelete, ProfileView, ProfileEdit

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('post/edit/<int:pk>',PostEdit.as_view(),name='post-edit'),
    path('post/delete/<int:pk>', PostDelete.as_view(),name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDelete.as_view(),name='comment-delete'),
    path('profile/<int:pk>', ProfileView.as_view(),name='profile'),
    path('profile/edit/<int:pk>', ProfileEdit.as_view(), name='profile-edit'),
]