from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import ItemListSerializer
from ..models import ItemList
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from location.models import Locations

class UserItemList(generics.ListAPIView):
    queryset = ItemList.objects.filter(user=1)
    serializer_class = ItemListSerializer


class ItemListAV(APIView):
    def get(self, request):
        items = ItemList.objects.all()
        serializer = ItemListSerializer(
            items, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemListSerializer(data=request.data)
        location = Locations.objects.get(name=request.data['location'])
        if serializer.is_valid():
            serializer.save(user=self.request.user, location=location)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailAV(APIView):
    def get(self, request, pk):
        try:
            item = ItemList.objects.get(pk=pk)
        except ItemList.DoesNotExist:
            return Response({'Error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ItemListSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = ItemList.objects.get(pk=pk)
        serializer = ItemListSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = ItemList.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def movielist(request):
#     if request.method == 'GET':
#         items = Movie.objects.all()
#         serializer = movieSerializer(items, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = movieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def moviedetails(request, pk):
#     if request.method == 'GET':
#         try:
#             item = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error' : 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = movieSerializer(item)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         item = Movie.objects.get(pk=pk)
#         serializer = movieSerializer(item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors)

#     if request.method == 'DELETE':
#         item = Movie.objects.get(pk=pk)
#         item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
