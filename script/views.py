from django.http import JsonResponse

def book_list(request):
    books = Book.objects.all().values('name', 'nationality', 'photo_url') # only grab some attributes from our database, else we can't serialize it.
    books_list = list(books) # convert our books to a list instead of QuerySet
    return JsonResponse(books_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.
