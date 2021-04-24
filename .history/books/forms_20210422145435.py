from django import forms
from .models import Book
from django.core.exceptions import ValidationError
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields='__all__'
      
    
    def clean_title(self):
        title=self.cleaned_data.get("title")
        if"test" in title:
            raise ValidationError("title shouldn't has test")
        return title

    def clean_title(self):
        title=self.cleaned_data.get("title")
        titleLength=len(title)
        
        if titleLength<10:
            raise ValidationError("title should be more than 10 chars!")
        if titleLength>50:
             raise ValidationError("title should be less than 20 chars!")
        return title