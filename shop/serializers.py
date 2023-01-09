from rest_framework import serializers

from .models import Category, Item, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ['profile', 'category']
        # read_only_fields = ['profile', ]