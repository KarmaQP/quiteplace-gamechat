from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .models import Post
from .models import Comment
from users.models import Account
from django.contrib.auth.models import User

from .forms import CommentForm

# Create your views here.


class AllBlogsPage(View):
  def get(self, request):
    all_posts = Post.objects.all()
    return render(request, 'blog/index.html', {
      'all_posts': all_posts
    })


class DetailBlogPage(View):
  def get(self, request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/detail_post.html', {
      'post': post,
      'post_tags': post.tags.all(),
      'comment_form': CommentForm(),
      'comments': Comment.objects.all().order_by('-id')
    })

  def post(self, request, slug):
    comment_form = CommentForm(request.POST)
    post = Post.objects.get(slug=slug)
    user = User.objects.get(username=request.user)

    if comment_form.is_valid:
      comment = comment_form.save(commit=False)
      comment.user = user
      comment.post = post
      comment.save()

      return HttpResponseRedirect(reverse('detail-blog-page', args=[slug]))
    else:
      context = {
        'post': post,
        'post_tags': post.tags.all(),
        'comment_form': comment_form,
        'comments': Comment.objects.all().order_by('-id')
      }
      return render(request, 'blog/post-detail.html', context)
