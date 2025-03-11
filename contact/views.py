from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact_us(request):
    """
    Handles contact form submissions and displays the Contact page.

    **Context**
    ``contact_form``
        A form for users to submit contact requests.

    **Template:**
    :template:`contact/contact.html`
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Contact request received!"
                                 " We endeavour to respond within 2 days.")
            contact_form = ContactForm()
        else:
            messages.add_message(request, messages.ERROR,
                                 "There was an error with your submission."
                                 " Please check the form and try again.")
    else:
        contact_form = ContactForm()  # Only reset on GET requests

    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form
        },
    )
