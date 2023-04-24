from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Products, Categories, LabelTag, Comment


@csrf_exempt
def add_to_cart(request):
    # Check if the request is a POST request
    if request.method == 'POST':
        productId = request.POST.get('productId')
        quantity = request.POST.get('qvalue')
        try:
            product = Products.objects.get(id=productId)
            product.cartquant = quantity
            serialized_product = serializers.serialize('json', [product])
            return JsonResponse({'data': serialized_product })

        except Products.DoesNotExist:
            return JsonResponse({'message': "No Such product is found "})

    else:
        return JsonResponse({'message': 'No request method is allowed'})

