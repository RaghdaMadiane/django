from django.contrib import admin
from .models import Book ,Category , Metric
from .forms import BookForm

class BookAdmin(admin.ModelAdmin):
    form=BookForm
    list_display=("title","author")
    list_filter=("categories",)
class BookInLine()    
class tagAdmin(admin.ModelAdmin):
    inlines=[BookInLine]    

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Metric)
