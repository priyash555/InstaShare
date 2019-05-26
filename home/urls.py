from django.contrib import admin
from django.urls import path, include
from .views import starting, PostListView, ModelCreateView, ModelUpdateView, ModelDetailView, ModelDeleteView, UserListView


urlpatterns = [
    path('', PostListView.as_view(), name='home-home'),
    path('create/', ModelCreateView.as_view(), name="home-createpost"),
    path('update/<int:pk>/', ModelUpdateView.as_view(), name="home-updatepost"),
    path('detail/<int:pk>/', ModelDetailView.as_view(), name="home-detailpost"),
    path('delete/<int:pk>/', ModelDeleteView.as_view(), name="home-deletepost"),
    path('user/<str:username>/', UserListView.as_view(), name="home-user"),
]