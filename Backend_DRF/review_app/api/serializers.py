from rest_framework import serializers
from ..models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('item',)
        # fields = "__all__"