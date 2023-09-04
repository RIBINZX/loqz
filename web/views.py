# Edit web/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can redirect to a success page or perform other actions.
            return redirect('/')  # Replace 'success_page' with the actual URL name or path.

    else:
        form = ContactForm()
    return render(request, "index.html", {'form': form})

