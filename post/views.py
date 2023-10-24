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
    print(queryset)
    serializer = PostSerializer(queryset, many=True)  #<QuerySet [<Post: Iphone>]>
    print(serializer.data)
    return Response(serializer.data)

    [
    {
        "category": 1,
        "title": "Iphone",
        "body": "Good phone",
        "created_at": "2023-10-24T05:10:55.275222Z"
    }
    ]

