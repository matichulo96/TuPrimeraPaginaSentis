from django import forms
from .models import Author, Book, Publisher

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'country']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'year']
        
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'rate']
        

class SearchBookForm(forms.Form):
    query = forms.CharField(label='Buscar libro')
