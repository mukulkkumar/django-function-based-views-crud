from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CardForm
from .models import Card

# Create your views here.
def home(request):
    cards = Card.objects.all()
    return render(request, 'index.html', { 'cards': cards })

def create(request):
    form = CardForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('index')
    context = {
        "form": form
    }
    return render(request, 'forms.html', context)

def update(request, id=None):
    instance = get_object_or_404(Card, id=id)
    form = CardForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
        return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'forms.html', context)

def delete(request, id=None):
    instance = get_object_or_404(Card, id=id)
    instance.delete()
    return redirect('index')
