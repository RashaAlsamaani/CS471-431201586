from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("list_books/", views.list_books, name="list_books"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("viewbook/<int:bookId>/", views.viewbook, name="view_one_book"),
    path('lab9/task6', views.lab9_task6, name='lab9_task6'), # lab 9-task 6
]
