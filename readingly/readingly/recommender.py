from .supabase_client import supabase


def recommend_based_on_favourite_genres(user_id):
    try:
 
        user_data = supabase.table("users").select("favourite_genres").eq("id", user_id).execute().data
        if not user_data:
            raise Exception("User not found")

        favourite_genres_ids = user_data[0]["favourite_genres"]

     
        genres_data = supabase.table("genres").select("name").in_("id", favourite_genres_ids).execute().data

  
        favourite_genres = [genre["name"] for genre in genres_data]


      
        books = (
            supabase.table("books")
            .select("*")
            .in_("genre", favourite_genres)
            .execute()
            .data
        )

        return books
    except Exception as e:
        raise Exception(f"Error fetching recommendations: {e}")


def recommend_highly_rated_books(user_id):
    try:
     
        user_data = supabase.table("users").select("not_interested_books","rated_books").eq("id", user_id).execute().data
        if not user_data:
            raise Exception("User not found")

        not_interested_books_ids = user_data[0]["not_interested_books"]
        rated_books = user_data[0]["rated_books"] 


        highly_rated_books_ids = [book['bookId'] for book in rated_books if book['rating'] >= 4]

       

        books_query = (
            supabase.table("books")
            .select("*")
        )

        if highly_rated_books_ids:
            books_query = books_query.in_("id", highly_rated_books_ids)
        else:
            return []

          
           
        if not_interested_books_ids:
            for book_id in not_interested_books_ids:
                books_query = books_query.neq("id", book_id)

        books = books_query.execute().data  

        
        return books
    except Exception as e:
        raise Exception(f"Error fetching recommendations: {e}")


def recommend_books_similar_to_read(user_id):
    try:
  
        user_data = supabase.table("users").select("read_books").eq("id", user_id).execute().data
        if not user_data:
            raise Exception("User not found")

        read_books = user_data[0]["read_books"]

     
        read_books_data = (
            supabase.table("books").select("genre").in_("id", read_books).execute().data
        )

        read_genres = list(set(book["genre"] for book in read_books_data))


        recommended_books = (
            supabase.table("books")
            .select("*")
            .in_("genre", read_genres)
            .execute()
            .data
        )

        recommended_books = [book for book in recommended_books if book["id"] not in read_books]

        return recommended_books
    except Exception as e:
        raise Exception(f"Error fetching recommendations: {e}")


