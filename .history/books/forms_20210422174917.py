from django import forms
from .models import Book ,Isbn
from django.core.exceptions import ValidationError
class IsbnForm(forms.ModelForm):
    class Meta:
        model = Isbn
        fields='__all__'
    def clean_title(self):

        title=self.cleaned_data.get("title")
        titleLength=len(title)
        
        if titleLength<10:
            raise ValidationError("title should be more than 10 chars!")
        if titleLength>50:
            raise ValidationError("title should be less than 20 chars!")
        return title    


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields='__all__'
      
    


   
    def clean_category(self):
        category=self.cleaned_data.get("category")
        catLength=len(category)
        if catLength<2:
            raise ValidationError("category name length should be more than 2 chars!")