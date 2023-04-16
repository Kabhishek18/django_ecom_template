from django.shortcuts import render, get_object_or_404
from .models import DynamicPage


def dynamic_page_view(request, pk):
    dynamic_page = get_object_or_404(DynamicPage, pk=pk)
    context = {'dynamic_page': dynamic_page}
    return render(request, 'v1/dynamic_page.html', context)
