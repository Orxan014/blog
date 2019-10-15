from rest_framework.generics import ListAPIView
from post.models import Post

class PostListAPIView(ListAPIView):
    query_set = Post.objects.all()