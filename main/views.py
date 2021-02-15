from django.shortcuts import render


def home_page(request):
    """Render home page and display Login link"""

    return render(request, "home.html", {"page_title": "Home"})
