"""
URL configuration for readingly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Recommender endpoints
    path('recommend/favourite-genres/<int:user_id>/', views.recommend_by_favourite_genres, name="recommend_by_favourite_genres"),
    path('recommend/highly-rated/<int:user_id>/', views.recommend_highly_rated, name="recommend_highly_rated"),
    path('recommend/similar-to-read/<int:user_id>/', views.recommend_similar_to_read, name="recommend_similar_to_read"),
]

