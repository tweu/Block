from post.models import Post
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = Post
    template_name ='post/index.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
