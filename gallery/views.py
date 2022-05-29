from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from .models import Location, Category, Image
from django.core.exceptions import ViewDoesNotExist





# Create your views here.
def home(request):
  #get all images
    images = Image.objects.all()
    print(images[0].category)
    arr= np.array(images) 
    newarr = np.array_split(arr,3)
    first = newarr[0]
    second = newarr[1]
    third = newarr[2]
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {"first": first,"second": second,"third": third,"locations": locations,"categories": categories})



#search_results function
def search(request):
  if 'category' in request.GET and request.GET["category"]:
    search = request.GET.get("category")
    try:
      category = Category.objects.get(name = search)
      images = Image.search_image(category)
      arr = np.array(images)
      newarr = np.array_split(arr,3)
      first = newarr[0]
      second = newarr[1]
      third = newarr[2]
      message = f"Found {len(images)} image(s) in this category - {search}"
      return render(request, 'search.html',{"message":message,"images": images,"first": first,"second": second,"third": third})
    except ViewDoesNotExist:
            message = "No items in this category " + search.upper()
            categories = Category.objects.all()
            return render(request, 'search.html',{"message":message, "categories": categories}) 



#display image in names location
def location(request, location_id):
    locations = Location.objects.all()
    images = Image.objects.filter(location_id=location_id)
    location = Location.objects.get(id=location_id)
    title = location
    return render(request, 'location.html', {'images': images, 'locations': locations, 'title': title})
    


