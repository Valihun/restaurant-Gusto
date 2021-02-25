from django.contrib import admin
from .models import Category, Dish, Event, Banners, UserMessages

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Event)
admin.site.register(Banners)
admin.site.register(UserMessages)
