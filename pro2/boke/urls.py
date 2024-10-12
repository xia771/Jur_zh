from django.urls import path
from .views import post_list, post_detail, add_comment

urlpatterns = [
    # path('post_list/', post_list, name='post_list'),
    # path('post_detail/', post_detail, name='post_detail'),
    # path('add_comment/', add_comment, name='add_comment'),
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/add_comment/', add_comment, name='add_comment'),
]