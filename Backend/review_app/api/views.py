from ..models import Review
from item_app.models import ItemList
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from .serializers import ReviewSerializer
from .permissions import IsUser
from rest_framework.permissions import IsAuthenticated

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        item = ItemList.objects.get(pk=pk)
        user = self.request.user
        review_queryset = Review.objects.filter(
            item=item, user=self.request.user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this item!")

        item.number_rating += 1
        temp = item.number_rating
        item.avg_rating = item.avg_rating * \
            ((temp-1)/temp) + serializer.validated_data['rating']/temp
        item.avg_rating = round(item.avg_rating, 2)
        item.save()

        serializer.save(item=item, user=self.request.user)


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    # permission_classes = [IsAuthenticated, IsUser]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(item=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_destroy(self, instance):
        item = instance.ItemList
        temp = item.number_rating
        item.avg_rating = (item.avg_rating -
                            (instance.rating/temp)) * (temp/(temp-1))
        item.number_rating -= 1
        item.save()
        instance.delete()

    def perform_update(self, serializer):
        pk = self.kwargs['pk']
        # hudai = self.hudai(2, 6, b=3, d=5)
        review = Review.objects.get(pk=pk)
        item = review.ItemList
        item.avg_rating = item.avg_rating + \
            (serializer.validated_data['rating'] -
             review.rating)/item.number_rating
        item.save()
        serializer.save()

    # def hudai(self, a, *args, **kwargs):
    #     rk = self.kwargs['pk']
    #     if args[0] != 0:
    #         raise ValidationError('rk='+str(rk)+
    #             ' a='+str(a)+' args[0]='+str(args[0])+' args[1]='+str(args[1])+\
    #             ' kwargs[b]='+str(kwargs['b'])+' kwargs[c]='+str(kwargs['c']))

# class ReviewDetail(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
