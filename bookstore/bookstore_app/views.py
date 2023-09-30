from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, PublisherForm, SearchBookForm
from .models import Book

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def insert_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuthorForm()
    
    return render(request, 'insert_author.html', {'form': form})

def insert_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()
    
    return render(request, 'insert_book.html', {'form': form})

def insert_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PublisherForm()
    
    return render(request, 'insert_publisher.html', {'form': form})

def search_book(request):
    if request.method == 'POST':
        form = SearchBookForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)  
            return render(request, 'search_results.html', {'results': results, 'query': query})
    else:
        form = SearchBookForm()
    
    return render(request, 'search_book.html', {'form': form})

def search_results(request):
    return render(request, 'search_results.html')
