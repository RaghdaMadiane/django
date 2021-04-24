from django.contrib import admin
from .models import Book ,Category ,Tag,Isbn
from django import forms
from django.core.exceptions import ValidationError

class BookForm(admin.ModelAdmin):
    class Meta:
        model = Book
        fields='__all__'

    def clean_title(self):
        title=self.cleaned_data.get("title")
        titleLength=len(title)
        if titleLength<10:
            raise ValidationError("title should be more than 10 chars!")
        if titleLength>20:
            raise ValidationError("title should be less than 20 chars!")
        return title

    def clean_category(self):
        category=self.cleaned_data.get("category")
        catLength=len(category)
        if catLength<2:
            raise ValidationError("category name length should be more than 2 chars!")
        return category

class BookAdmin(admin.ModelAdmin):
    form=BookForm
    
    list_filter=("categories",)

class BookInLine(admin.StackedInline):
    model=Book
    max_num =3
    extra =  1  
class TagAdmin(admin.ModelAdmin):
    inlines=[BookInLine]    
class IsbnAdmin(admin.ModelAdmin):
     inlines=[BookInLine]
admin.site.register(Book,BookAdmin)
admin.site.register(Category)
admin.site.register(Isbn,IsbnAdmin)
admin.site.register(Tag,TagAdmin)




