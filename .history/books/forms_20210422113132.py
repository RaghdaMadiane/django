from django import forms
from .models import Book
from django.core.exceptions import ValidationError
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields='__all__'
        exclude=("metrics",)
    
    def clean_title(self):
        title=self.cleaned_data.get("title")
        if"test" in title:
            raise ValidationError("title shouldn't has test")
        return title

    def clean(self):   # btt2kd 2no valid 
        super(BookForm,self).clean()
        content=self.cleaned_data.get('content')
        