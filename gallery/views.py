from django.shortcuts import render
from django.http import HttpResponse
from .models import Location, Category, Image
from django.core.exceptions import ViewDoesNotExist





# Create your views here.
def home(request):
  #get all images
  images = Image.objects.all().order_by('-id')
  locations = Location.objects.all()
  categories = Category.objects.all()
  return render(request, 'home.html', {"images":images,"locations": locations,"categories": categories})


#search_results function
def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category").lower()
        searched_images = Image.filter_by_category(search_term)
        message = f"{search_term}"
        locations = Location.objects.all()
        categories = Category.objects.all()
        return render(request, 'search.html',{"message":message, "categories": categories}) 

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})
