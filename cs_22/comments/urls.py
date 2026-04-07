from django.urls import path
from .views import create_comment
from .views import CommentListAPIView, CommentRetrieveAPIView


urlpatterns = [
    path('', CommentListAPIView.as_view(), name='comment-list'),
    path('<int:pk>', CommentRetrieveAPIView.as_view(), name='comment-detail'),
    path('create/', create_comment, name='create_comment'),
]
