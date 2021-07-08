from django.urls import path
from post import views


urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('/<int:post_id>/', views.PostDetail.as_view(), name = 'post_detail'),
]