from django.urls import path
from .views import login, form, home

urlpatterns = [
    path('', login),
    path('home', home),
    path('records',form.as_view())
]