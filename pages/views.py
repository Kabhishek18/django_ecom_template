from django.shortcuts import render, get_object_or_404
from products.models import Products, Categories, LabelTag, Comment
from .models import DynamicPage


# Product Main Page Is From Here
def index(request):
    categories = Categories.objects.all()
    products = Products.objects.all()
    data = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'v1/index.html', data)


# Creating Dynamic Page form Here:
def dynamic_page_view(request, etitle):
    try:
        page = DynamicPage.objects.get(slug=etitle)
        dynamic_page = {
            'title': page.title,
            'content':  page.content,
            'meta_tag' : page.meta_tag,
        }
        return render(request, 'v1/dynamic_page.html', dynamic_page)

    except:
        dynamic_page = {
            'title': "404 Page",
            'content': "content"
        }
        return render(request, 'v1/404.html', dynamic_page)


def custom_404(request, exception):
    return render(request, '404.html', status=404)
