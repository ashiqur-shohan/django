from django.shortcuts import render
from car_model.models import CarModel
from brand.models import BrandModel


# def home(request):
#     data = CarModel.objects.all()
#     brands = BrandModel.objects.all()
#     return render(request,'home.html',{'data': data, 'brand': brands})

def home(request,brand_slug=None):
    data = CarModel.objects.all()
    if brand_slug is not None:
        brand = BrandModel.objects.get(slug=brand_slug)
        data = CarModel.objects.filter(brand=brand)
    brands = BrandModel.objects.all()
    return render(request,'home.html',{'data': data, 'brand': brands})