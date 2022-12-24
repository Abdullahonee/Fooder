from rest_framework import serializers
from order_app.api.serializers import OrderSerializer
from review_app.api.serializers import ReviewSerializer
from ..models import ItemList

class ItemListSerializer(serializers.ModelSerializer):
    orderlist = OrderSerializer(many=True, read_only=True)
    reviewlist = ReviewSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)
    location = serializers.StringRelatedField(read_only=True)
    total_available = serializers.StringRelatedField(read_only=True)

    def get_avg_rating(self, obj):
        return round(obj.avg_rating, 1)
    # len_name = serializers.SerializerMethodField()
    # url = serializers.HyperlinkedIdentityField(view_name='ItemList-detail')

    class Meta:
        model = ItemList
        fields = "__all__"
        # extra_kwargs = {
        #     'order_count' : {'read_only' : True},
        #     'number_rating' : {'read_only' : True},
        # }

        # fields = ['id', 'name', 'comment']
        # exclude = ['name']

    # def get_len_name(self, object):
    #     return len(object.name)

    # def validate(self, data):
    #     if data['name'] == data['comment']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

# class movieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     comment = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.comment = validated_data.get('comment', instance.comment)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['comment']:
#             raise serializers.ValidationError("Title and Description should be different!")
#         else:
#             return data

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value
