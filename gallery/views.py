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



#search function
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
  else:
        message = "You haven't searched any category"
        return render(request, 'search.html',{"message":message})



#display image in named location
def location(request, location_id):
    try:
        location = Location.objects.get(id=location_id)
        images = Image.filter_by_location(location)
        arr= np.array(images) 
        newarr = np.array_split(arr,3)
        first = newarr[0]
        second = newarr[1]
        third = newarr[2]
        message = location.name
        title = location.name
        return render(request, 'search.html',{"title":title, "message":message,"images": images,"first": first,"second": second,"third": third})
    except ViewDoesNotExist:
        message = "No items in this location"
        locations = Location.objects.all()
        title= "Not Found"
        return render(request, 'search.html',{"title":title,"message":message, "locations": locations})

#display image in named category
def category(request, category_id):
    try:
        category = Category.objects.get(id = category_id)
        images = Image.search_image(category)
        arr= np.array(images) 
        newarr = np.array_split(arr,3)
        first = newarr[0]
        second = newarr[1]
        third = newarr[2]
        message = category.name
        title = category.name
        return render(request, 'search.html',{"title":title, "message":message,"images": images,"first": first,"second": second,"third": third})
    except ViewDoesNotExist:
        message = "No items in this location" + search.upper()
        categories = Category.objects.all()
        title= "Not Found"
        return render(request, 'search.html',{"title":title,"message":message, "categories": categories})
    
#image 

def image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
        print(image.category.id)
    except ViewDoesNotExist:
        message = "No image to display or image deleted"
        return render(request, 'image.html', {"message":message})
    return render(request, 'image.html', {"image":image})  


