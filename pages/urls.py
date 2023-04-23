from django.urls import path
from .views import dynamic_page_view, index,custom_404


urlpatterns = [
    path('<str:etitle>/', dynamic_page_view, name='dynamic_page'),
    path('', index, name='home'),
    path('404/', custom_404),
]
