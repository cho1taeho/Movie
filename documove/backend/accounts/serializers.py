from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Wishlist
from movies.models import Movie
from movies.serializers import MovieWishlistSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'point', 'badge',)

class WishlistSerializer(serializers.ModelSerializer):
    moives = MovieWishlistSerializer(many=True)
    
    class Meta:
        model = Wishlist
        fields = ['user', 'movies', 'created_at']


class UserbadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'badge',)