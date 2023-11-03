from django.urls import path
from consulta.views import index, SearchView

urlpatterns = [
    path('', index),
    path('search', SearchView.as_view()),
    ]