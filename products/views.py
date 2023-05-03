from django.shortcuts import render
from .models import Products, Categories, LabelTag, Comment


# Create your views here.
def index(request):
    categories = Categories.objects.all()
    products = Products.objects.all()
    data = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'v1/index.html', data)
