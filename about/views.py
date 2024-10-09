from django.shortcuts import render
from .models import About
from django.contrib import messages
from .forms import ContactRequestForm


# Create your views here.
def about_site(request):
    """
    Renders the most recent information on the website author
    and allows the collaboration requests
    Displays an individual instance of :model:`about.About`.
    **Template**
    :template:`about/about.html`
    """

    if request.method == "POST":
        contact_form = ContactRequestForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request,
                             'Contact request received!'
                             ' I endeavor to respond '
                             'within 2 working days.'
                             )

    about = About.objects.all()
    contact_form = ContactRequestForm()

    return render(
        request,
        "about/about.html",
        {
         "about": about,
         "contact_form": contact_form
         },
    )
