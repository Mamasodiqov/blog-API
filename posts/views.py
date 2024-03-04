from django.shortcuts import render

from django.contrib.auth import get_user_model
from .serializers import PostSerializer , UserSerializer
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet 
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from .models import Post
# Create your views here.

class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
    #Quyidagi o`xshash kodlarni qisqartiradigan yuqoridagi kabi ViewSet lar mavjud
# class PostList(ListCreateAPIView):
#     
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
    
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
# class UserList(ListCreateAPIView):
    
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(RetrieveUpdateDestroyAPIView):
#     
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
    