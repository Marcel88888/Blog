from django.urls import path
from blog import views


urlpatterns = [
    path('', views.PostsListView.as_view(), name='posts_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>', views.PostDetailsView.as_view(), name='post_details'),
    path('post/new/', views.CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    path('drafts/', views.DraftsListView.as_view(), name='drafts_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.approve_comment, name='approve_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('post/<int:pk>/publish', views.publish_post, name='publish_post'),
]