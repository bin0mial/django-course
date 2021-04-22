from django.urls import path

from . import views

app_name = 'Books'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name="create"),
    path('edit/<int:book_id>', views.update, name="edit"),
    path('delete/<int:book_id>', views.delete, name="delete"),
]
