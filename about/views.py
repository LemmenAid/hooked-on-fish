from django.shortcuts import render
from django.http import HttpResponse
from .models import About


def about_me(request):
    """
    Renders the About page with the most recent content.
    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.

    **Template:**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    # If no About object exists, provide a fallback message
    if not about:
        about = None

    return render(
        request,
        "about/about.html",
        {"about": about,
         "no_about_content": not about},
    )