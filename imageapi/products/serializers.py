from . models import Category, Product, ProductImage
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ["category_id", "title"]

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductImage
        fields= ["id", "product", "image"]


class ProductSerializer(serializers.ModelSerializer):
    images =ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(child=serializers.ImageField(max_length=1000, allow_empty_file=False, use_url=False),write_only=True)
    class Meta:
        model= Product
        fields= ["id", "name", "description", "category", "images", "uploaded_images"]

    def create(self, validate_data):
        uploaded_images= validate_data.pop("uploaded_images")
        product= Product.objects.create(**validated_data)
        for image in uploaded_images:
            newproduct_image= ProductImage.objects.create(product=product, image=image)

        return product



