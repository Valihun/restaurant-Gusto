from django.shortcuts import render
from main_gusto.models import Dish
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
# Напомнить Эдварду чтобы рассказал что происходит после того, как нажимаем на категорию "Салаты"
def dish_info(request, category):
    try:
        dishes = Dish.objects.all()
        return render(request, 'dish.html', context={'category': dishes, })
    except Dish.DoesNotExist:
        return HttpResponseNotFound("Page not found")
