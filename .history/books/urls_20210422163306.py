
from django.urls import path
from . import views

urlpatterns = [
   path("",views.index,name='index'),
   path("create",views.create, name='create'),
   path("edit/<str:isbn>",views.edit, name='edit'),
  path('delete/<str:isbn>', views.delete, name='delete'),  
]