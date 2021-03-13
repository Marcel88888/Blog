from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostsListView(ListView):
    model = Post

    def get_queryset(self):
        #  'lte' - less than or equal to
        return Post.objects.filter(publication_date__lte=timezone.now().order_by('-published_date'))


class PostDetailsView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_details.html'
    form_class = PostForm
    model = Post
