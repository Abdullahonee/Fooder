from rest_framework import generics
from rest_framework.response import Response
# from .serializers import FindSerializer
from item_app.models import ItemList
from item_app.api.serializers import ItemListSerializer
from user_app.models import User
from location.models import LocationDist
from location.api.serializers import LocationDistSerializer
import re


class FindList(generics.ListAPIView):
    # serializer_class = FindSerializer
    
    def get(self, request, *args, **kwargs):
        
        # def cmp_dist_rating(a, b):
        #     if a[0] != b[0]:
        #         return a[0] < b[0]
        #     return a[1].avg_rating > b[1].avg_rating
        
        # def cmp_dist_price_asc(a, b):
        #     if a[0] != b[0]:
        #         return a[0] < b[0]
        #     return a[1].price < b[1].price
    
        # def cmp_dist_price_dsc(a, b):
        #     if a[0] != b[0]:
        #         return a[0] < b[0]
        #     return a[1].price > b[1].price
        
        queryset = ItemList.objects.all()
        # queryset = ItemList.objects.filter(title=request.GET.get('title'))
        # return Response(ItemListSerializer(queryset, many=True, context={'request': request}).data)
        title=request.GET.get('title')
        user_location = request.GET.get('location')
        prefer_dist = float(request.GET.get('dist'))
        querylist = []

        for item in queryset:
            if re.search(title.lower(), item.title.lower()):
                product_location = item.location.name
                dist = LocationDist.objects.filter(start__startswith=user_location) & LocationDist.objects.filter(
                    end__startswith=product_location)
            
                for d in dist:
                    if d.distance <= prefer_dist:
                        t = (d.distance, item)
                        querylist.append(t)
                        
        for item in queryset:
            if re.search(title.lower(), item.title.lower()) and item.location.name == user_location:
                t = (0, item)
                querylist.append(t)
                        
                # querylist.append(item)

        # rating_des = request.GET.get('rating')
        # price_asc = request.GET.get('price_asc')
        final = []
        # if rating_des == "True":
        #     final = sorted(querylist, key=functools.cmp_to_key(cmp_dist_rating))
        # elif price_asc == "True":
        #     final = sorted(querylist, key=functools.cmp_to_key(cmp_dist_price_asc))
        # elif price_asc != "True":
        #     final = sorted(querylist, key=functools.cmp_to_key(cmp_dist_price_dsc))
        # else:
        #     final = sorted(querylist, key=lambda x: x[0])
        final = sorted(querylist, key=lambda x: x[0])
                
        # querylist = sorted(querylist, key=lambda x: x[0])
        searched_items = []
        # searched_items = querylist

        for x in final:
            searched_items.append(x[1])

        item_serializer = ItemListSerializer(
            searched_items, many=True, context={'request': request})
        return Response(item_serializer.data)
