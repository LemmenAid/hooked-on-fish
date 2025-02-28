from django.shortcuts import render
from .models import About, Grounds


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


def grounds(request):
    """
    Renders the Fishing Grounds page with the most recent content.
    Displays an individual instance of :model:`grounds.Grounds`.

    **Context**
    ``grounds``
        The most recent instance of :model:`grounds.Grounds`.

    **Template:**
    :template:`about/grounds.html`
    """
    grounds = Grounds.objects.all().order_by('-updated_on').first()

    # If no About object exists, provide a fallback message
    if not grounds:
        grounds = None

    return render(
        request,
        "about/grounds.html",
        {"grounds": grounds,
         "no_grounds_content": not grounds},
    )
