from django.shortcuts import render
from django.contrib import messages
from .models import Contact
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

    contact = Contact.objects.all()
    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form
        },
    )
