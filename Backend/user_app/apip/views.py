from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from ..models import User
from rest_framework import generics
from rest_framework.settings import api_settings
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }


class UserRegister(APIView):

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data['password']
        password2 = serializer.validated_data['password2']
        email = serializer.validated_data['email']
        username = serializer.validated_data['username']
        if password != password2:
            raise ValidationError("Passwords must be same!")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists!")
        user = User(email=email, username=username)
        user.set_password(password)
        user.save()
        data = {}
        data['response'] = "Registration successful!"
        data['username'] = username
        data['email'] = email
        data['token'] = user.tokens
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class UserLogin(APIView):

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def post(self, request):
        # serializer = UserLoginSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        password = request.POST['password']
        # username = request.POST['username']
        email = request.POST['email']
        # headers = self.get_success_headers(serializer.data)
        user = authenticate(email=email, password=password)
        if user is not None:
            data = {}
            data['response'] = "Login successful!"
            # data['username'] = username
            data['email'] = email
            data['token'] = user.tokens
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND, headers=headers)
        

class UserLogout(APIView):

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserOrders(generics.ListAPIView):
#     serializer_class = OrderSerializer

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return Order.objects.filter(User=pk)


# class UserItems(generics.ListCreateAPIView):
#     serializer_class = ItemListSerializer

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return ItemList.objects.filter(User=pk)

#     def perform_create(self, serializer):
#         pk = self.kwargs['pk']
#         pkStore = serializer.validated_data['store']
#         User = User.objects.get(pk=pk)
#         User.item_count += 1
#         User.save()
#         store = Store.objects.get(pk=pkStore)
#         store.item_count += 1
#         store.save()
#         serializer.save(User=User, store=store)


# class UserStoreItems(generics.ListCreateAPIView):
#     serializer_class = ItemListSerializer

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         pkStore = self.kwargs['pkStore']
#         return ItemList.objects.filter(User=pk, store=pkStore)

#     def perform_create(self, serializer):
#         pk = self.kwargs['pk']
#         pkStore = self.kwargs['pkStore']
#         User = User.objects.get(pk=pk)
#         User.item_count += 1
#         User.save()
#         store = Store.objects.get(pk=pkStore)
#         store.item_count += 1
#         store.save()
#         serializer.save(User=User, store=store)


# class UserItemOrders(generics.ListAPIView):
#     serializer_class = OrderSerializer

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         pkItem = self.kwargs['pkItem']
#         return Order.objects.filter(User=pk, item=pkItem)


# class UserStores(generics.ListAPIView):
#     serializer_class = StoreSerializer

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return Store.objects.filter(User=pk)

#     def perform_create(self, serializer):
#         pk = self.kwargs['pk']
#         User = User.objects.get(pk=pk)
#         User.store_count += 1
#         User.save()
#         serializer.save(User=User)


# class UserStoreOrders(generics.ListAPIView):
#     serializer_class = OrderSerializer

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         pkStore = self.kwargs['pkStore']
#         return Order.objects.filter(User=pk, store=pkStore)
