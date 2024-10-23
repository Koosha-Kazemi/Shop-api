from rest_framework.serializers import ModelSerializer

from .models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class OptionProductSerializer(ModelSerializer):
    class Meta:
        model = OptionProduct
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = 'image/'