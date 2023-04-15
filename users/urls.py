from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from . import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
    path('login/', user_view.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='v1/index.html'), name='logout'),
    path('register/', user_view.register, name='register'),
]