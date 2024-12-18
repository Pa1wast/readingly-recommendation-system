from .supabase_client import supabase
from django.http import JsonResponse

from .recommender import (
    recommend_based_on_favourite_genres,
    recommend_highly_rated_books,
    recommend_books_similar_to_read,
)

# Recommend books based on favourite genres
def recommend_by_favourite_genres(request, user_id):
    try:
        recommendations = recommend_based_on_favourite_genres(user_id)
        return JsonResponse({"status": "success", "data": recommendations}, status=200)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


# Recommend highly-rated books
def recommend_highly_rated(request, user_id):
    try:
        recommendations = recommend_highly_rated_books(user_id)
        return JsonResponse({"status": "success", "data": recommendations}, status=200)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


# Recommend books similar to those the user has read
def recommend_similar_to_read(request, user_id):
    try:
        recommendations = recommend_books_similar_to_read(user_id)
        return JsonResponse({"status": "success", "data": recommendations}, status=200)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

