import requests
from django.http import JsonResponse

# def get_books(request):
#     url = 'https://openlibrary.org/search.json?q=love'
#     try:
#         response = requests.get(url)
#         response.raise_for_status() 
#         data = response.json()
#         return JsonResponse(data.get('docs', []), safe=False)
#     except requests.RequestException as e:
#         return JsonResponse({"error": str(e)}, status=500)

# def get_book(request, id):
#     url = f'https://openlibrary.org/works/{id}.json'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         return JsonResponse(data)
#     except requests.RequestException as e:
#         return JsonResponse({"error": str(e)}, status=500)

# def get_cover(request, id):
#     size = request.GET.get('size', 's').upper()
#     url = f'https://covers.openlibrary.org/b/id/{id}-{size}.jpg'
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return JsonResponse({"image_url": url})
#         else:
#             return JsonResponse({"error": "Cover not found"}, status=404)
#     except requests.RequestException as e:
#         return JsonResponse({"error": str(e)}, status=500)
