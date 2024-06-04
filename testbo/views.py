from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework.response import Response


# Create your views here.
class PostView(APIView):
    def get(self, request, pk=None):
        post = Post.objects.all()
        serializer = PostSerializer(instance=post, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        post = Post.objects.get(id=pk)
        post.delete()
        return Response()


class CommentView(APIView):
    def get(self, request, pk=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(instance=comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        comment.delete()
        return Response()