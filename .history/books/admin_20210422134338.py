from django.contrib import admin
from .models import Book ,Category ,Isbn
from .forms import BookForm

class BookAdmin(admin.ModelAdmin):
    form=BookForm
    list_display=("title","author")
    list_filter=("categories",)


admin.site.register(Book,BookAdmin)
admin.site.register(Category)
admin.site.register(Isbn)
# admin.site.register(Tag,TagAdmin)
