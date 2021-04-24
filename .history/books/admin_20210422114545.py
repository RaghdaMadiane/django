from django.contrib import admin
from .models import Book ,Category , Metric

class BookAdmin(admin.ModelAdmin):
    list_display=("title","author")


admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Metric)
