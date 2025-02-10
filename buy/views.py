from django.shortcuts import render
from django.http import HttpResponse
from .models import BuyOnline, BuyInPerson


def buy_online(request):
    """
    Renders the Buy Online page with the most recent content.
    Displays an individual instance of :model:`buy_online.BuyOnline`.

    **Context**
    ``buy_online``
        The most recent instance of :model:`buy_online.BuyOnline`.

    **Template:**
    :template:`buy/buy_online.html`
    """
    buy_online = BuyOnline.objects.all().order_by('-updated_on').first()

    # If no About object exists, provide a fallback message
    if not buy_online:
        buy_online = None

    return render(
        request,
        "buy/buy_online.html",
        {"buy_online": buy_online,
         "no_buy_online_content": not buy_online},
    )


def buy_in_person(request):
    """
    Renders the Buy in Person page with the most recent content.
    Displays an individual instance of :model:`buy_in_person.BuyInPerson`.

    **Context**
    ``in_person``
        The most recent instance of :model:`buy_in_person.BuyInPerson`.

    **Template:**
    :template:`buy/buy_in_person.html`
    """
    buy_in_person = BuyInPerson.objects.all().order_by('-updated_on').first()

    # If no About object exists, provide a fallback message
    if not buy_in_person:
        buy_in_person = None

    return render(
        request,
        "buy/buy_in_person.html",
        {"buy_in_person": buy_in_person,
         "no_buy_in_person_content": not buy_in_person},
    )

