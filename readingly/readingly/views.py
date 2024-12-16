import os
from supabase import create_client, Client
from django.http import JsonResponse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase configuration
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)



def get_books(request):
    try:
        response = supabase.table("books").select("*").execute()
        books = response.data

        return JsonResponse({
            "status": "success",
            "data": books
        }, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)



def get_book(request, id):
    try:
        response = supabase.table("books").select("*").eq("id", id).execute()
        book = response.data

        if not book:
            return JsonResponse({
                "status": "error",
                "message": "Book not found"
            }, status=404)

        return JsonResponse({
            "status": "success",
            "data": book
        }, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)


# Function to get all users
def get_users(request):
    try:
        # Fetch all records from the 'users' table
        response = supabase.table("users").select("*").execute()
        users = response.data

        return JsonResponse({
            "status": "success",
            "data": users
        }, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)


# Function to get a single user by ID
def get_user(request, id):
    try:
        # Fetch a single record by ID from the 'users' table
        response = supabase.table("users").select("*").eq("id", id).execute()
        user = response.data

        if not user:
            return JsonResponse({
                "status": "error",
                "message": "User not found"
            }, status=404)

        return JsonResponse({
            "status": "success",
            "data": user
        }, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)
