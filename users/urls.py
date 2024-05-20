from users.apps import UsersConfig
from users.views import UserCreateView,UserListView,UserRetrieveView,UserUpdateView,UserDestroyView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


app_name = UsersConfig.name

urlpatterns = [
    path('create/',UserCreateView.as_view(),name='user_create'),
    path('',UserListView.as_view(),name='user_list'),
    path('view/<int:pk>',UserRetrieveView.as_view(),name='user_view'),
    path('edit/<int:pk>',UserUpdateView.as_view(),name='user_edit'),
    path('delete/<int:pk>',UserDestroyView.as_view(),name='user_delete'),
    path('token',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
]