from django.contrib import admin
from .models import Book ,Category , Metric ,Tag
from .forms import BookForm

class BookAdmin(admin.ModelAdmin):
    form=BookForm
    list_display=("title","author")
    list_filter=("categories",)
# class BookInLine(admin.ModelAdmin):
#     model=Book
#     max_num =3
#     extra =  1  
# class TagAdmin(admin.ModelAdmin):
#     inlines=[BookInLine]    

admin.site.register(Book,BookAdmin)
admin.site.register(Category)
# admin.site.register(Metric)
# admin.site.register(Tag,TagAdmin)
