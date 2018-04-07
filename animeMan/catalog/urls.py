from django.urls import path
from .views import login, form, home

urlpatterns = [
    path('', home),
    path('login', login),
    path('records',form.as_view()),
]