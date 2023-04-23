"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#Admin Url Config
admin.site.site_header = 'Ecommerce Krab Templates'
admin.site.site_title = 'Ecommerce | Krab '
admin.site.index_title = 'Krab Administration'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("products/", include('products.urls')),
    path("", include('pages.urls')),
    path("users/", include('users.urls')),
    # Api branching here
    path("v1/api/", include('apiset.urls')),
    path('v1/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
