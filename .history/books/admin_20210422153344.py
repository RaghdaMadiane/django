from django.contrib import admin
from .models import Book ,Category 
from .forms import BookForm

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields="_all_"

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

# admin.site.register(Tag,TagAdmin)




