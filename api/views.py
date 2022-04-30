from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Comment
from .serializers import CommentSerializer


@api_view(['GET'])
def getData(request):
  comments = Comment.objects.all()
  serializer = CommentSerializer(comments, many=True)
  return Response(serializer.data)


@api_view(['POST'])
def addComment(request):
  serializer = CommentSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)
