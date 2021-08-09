from rest_framework import serializers
from .models import Books

class BookAPI(serializers.ModelSerializer):
        class Meta:
            model = Books
            fields="__all__"