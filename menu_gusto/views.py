from django.shortcuts import render
from main_gusto.models import Dish
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
# Напомнить Эдварду чтобы рассказал что происходит после того, как нажимаем на категорию "Салаты"
def category(request, category):
    try:
        dishes = Dish.objects.filter(category=category)
        return render(request, 'dish.html', context={'category': dishes})
    except Dish.DoesNotExist:
        return HttpResponseNotFound("Page not found")


def dish(request, category, dish):
    dish = Dish.objects.get(pk=dish)
    return render(request, "dish_info.html", context={'dish': dish, 'category_id': category})
