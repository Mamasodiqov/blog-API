from django.urls import path
from .views import UserViewSet, PostViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls

#quyidagi kodni yuqoridagi kabi router orqali soddalashtirish mumkin

# urlpatterns = [
#     path('users/',UserList.as_view()),
#     path('users/<int:pk>/',UserDetail.as_view()),
#     path('<int:pk>/',PostDetail.as_view()),
#     path('',PostList.as_view()),
# ]
