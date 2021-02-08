from django.urls import path
from user_messages.views import messages_view


urlpatterns = [
    path('view/', messages_view),
]
