from rest_framework import serializers
from products.models import Products,Categories,LabelTag

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'