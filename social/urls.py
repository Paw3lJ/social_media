from django.urls import path
from .views import PostListView, PostDetail, PostEdit, PostDelete,CommentDelete, ProfileView, ProfileEdit, AddFollower, DeleteFollower, AddLike, DisLike, UserSearch, AddCommentLike, CommentDisLike, CommentReplyView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('post/edit/<int:pk>',PostEdit.as_view(),name='post-edit'),
    path('post/delete/<int:pk>', PostDelete.as_view(),name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDelete.as_view(),name='comment-delete'),
    path('profile/<int:pk>', ProfileView.as_view(),name='profile'),
    path('profile/edit/<int:pk>', ProfileEdit.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/add',AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/delete',DeleteFollower.as_view(), name='delete-follower'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', DisLike.as_view(), name='dislike'),
    path('search/', UserSearch.as_view(), name='profile-search'),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', CommentDisLike.as_view(), name='comment-dislike'),
    path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='comment-reply'),

]