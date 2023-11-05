from django.urls import path
from consulta.views import index, SearchView

urlpatterns = [
    path('', index, name='index'),
    path('search', SearchView.as_view()),
    ]