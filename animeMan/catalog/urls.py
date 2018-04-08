from django.urls import path
from .views import login_view, register_view, logout_view, form, home
from . import views

urlpatterns = [
    path('', home),
    path('records',form.as_view()),
    #path('register', loginView.as_view()),
    # url(r'^login/', login_view, name = 'login'),
    path('login', login_view),
    path('home/home.html', home),
    path('logout', logout_view),
]