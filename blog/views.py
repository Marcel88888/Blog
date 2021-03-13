from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostsListView(ListView):
    model = Post

    def get_queryset(self):
        #  'lte' - less than or equal to
        return Post.objects.filter(publication_date__lte=timezone.now()).order_by('-published_date')


class PostDetailsView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostEditView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftsListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = '/blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publication_date__isnull=True).order_by('creation_date')

###############################################################


@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_details', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'comment_form': form})


@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_details', pk=comment.post.pk)


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_details', pk=post_pk)
