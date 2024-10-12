from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from flask import redirect

from . import admin
from.models import Post, Comment
from django.core.paginator import Paginator


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'page_obj': page_obj})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comment_set.all()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if request.user.is_authenticated:
            Comment.objects.create(content=content, author_user=request.user, post=post)
        else:
            anonymous_name = request.POST.get('anonymous_name')
            Comment.objects.create(content=content, anonymous_name=anonymous_name, post=post)
        return redirect('post_detail', post_id)
    return render(request, 'add_comment.html', {'post': post})