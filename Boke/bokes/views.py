
# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, Comment
from django.core.paginator import Paginator

def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(posts, 5)  # 每页显示5篇文章
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'page_obj': page_obj})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        Comment.objects.create(post=post, content=request.POST['content'])
        return redirect('post_detail', pk=post.pk)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})