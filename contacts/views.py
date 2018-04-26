from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm
from .models import Contact

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'contacts': Contact.objects.all(),
                'form': ContactForm()}
    return render(request, 'contacts/contacts.html', context)
