from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("list_books/", views.list_books, name="list_books"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("viewbook/<int:bookId>/", views.viewbook, name="view_one_book"),
]
