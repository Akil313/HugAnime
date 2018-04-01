from django.urls import path
from .views import index, form

urlpatterns = [
    path('', index),
    path('records',form.as_view())
]