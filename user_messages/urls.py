from django.urls import path
from user_messages.views import messages_view, error


urlpatterns = [
    path('view/', messages_view),
    path('error/', error),
]
