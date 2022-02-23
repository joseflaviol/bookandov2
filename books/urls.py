from django.urls import path

from . import views

urlpatterns = [
    path('search/<str:title>', views.search, name="search"),
    path('book_details', views.book_details, name="book_details")
]
