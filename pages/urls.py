from django.urls import path
from .views import dynamic_page_view

urlpatterns = [
    path('<int:pk>/', dynamic_page_view, name='dynamic_page'),
]