from django.contrib import admin
from .models import Book ,Category ,Tag,Isbn
from .forms import BookForm ,IsbnForm
from django import forms
from django.core.exceptions import ValidationError



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
    form=IsbnForm
    inlines=[BookInLine]
admin.site.register(Book,BookAdmin)
admin.site.register(Category)
admin.site.register(Isbn,IsbnAdmin)
admin.site.register(Tag,TagAdmin)




