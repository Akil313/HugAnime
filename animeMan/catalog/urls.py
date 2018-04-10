from django.urls import path
from .views import login_view, logout_view, form, home
from . import views

urlpatterns = [
    path('', home),
    path('records',form.as_view()),
    path('login', login_view),
    path('home', home),
    path('logout', logout_view),
]