# about_macmassage/views.py
from django.shortcuts import render

def about_index(request):
    """
    View function for the about page.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered HTML response for the about page.
    """
    return render(request, 'about_index.html')