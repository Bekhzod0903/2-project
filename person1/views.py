from django.shortcuts import render
from .models import Person,Category
# Create your views here.

def get_info(request):
    categories = Category.objects.all()
    context={
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_person(request, pk):
    person = Person.objects.get(pk=pk)
    context = {'person': person}
    return render(request, 'person.html', context)