from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now())
    publication_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publication_date = timezone.now()
        self.save()

    def get_approved_comments(self):
        return self.comments.filter(approved=True)

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', max_length=200, on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now())
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('posts_list')

    def __str__(self):
        return self.text
