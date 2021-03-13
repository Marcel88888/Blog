from django.urls import path
from blog import views


urlpatterns = [
    path('', views.PostsListView.as_view(), name='posts_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>', views.PostDetailsView.as_view(), name='post_details'),
    path('post/new/', views.CreatePostView.as_view(), name='create_post'),
]