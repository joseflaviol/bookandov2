import requests
import json

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def search(request, title):
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + title + "&key=AIzaSyCZyt7FNEVc0RwmCIWmcx831Aoj6Ppr6so&fields=kind,items(id,volumeInfo(title,subtitle,authors,description,pageCount,categories,averageRating,imageLinks(thumbnail)))&orderBy=relevance")
    return JsonResponse(json.loads(r.text))

def book_details(request):
    return render(request, "book_details.html")
