from django.shortcuts import render
from .models import Post
# Create your views here.


def posts_list(request):
    queryset = Post.objects.all()
    return render(request, 'listing.html', {'posts': queryset})


"REST"

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def posts_list_api_view(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)  
    return Response(serializer.data)


@api_view(['GET'])
def post_details_api_view(request, id):

    # 1 вариант
    # post = Post.objects.get(id=id)
    # print(post)
    # serializer = PostSerializer(post)
    # print(serializer.data)


    # 2 вариант
    try:
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response('no id for this post')




