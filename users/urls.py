from django.urls import path
from .views import UserListView, UserDetailView, UserProfileListView, UserProfileDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('profiles/', UserProfileListView.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
]
