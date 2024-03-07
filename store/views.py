from rest_framework import generics
from rest_framework import status
from store.models import Sku,Transaction,Order,Client
from store.serializers import SkuSerializer, UserSerializer, TransactionSerializer,OrderSerializer,ClientSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from store.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response




# Sku
class SkuList(generics.ListCreateAPIView):
    queryset = Sku.objects.all()
    serializer_class = SkuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SkuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sku.objects.all()
    serializer_class = SkuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]


#User
class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=["get"])
    def getbyname(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=self.kwargs['username'])
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=UserSerializer(user)
        return Response(serializer.data)


#Transaction
class TransactionList(generics.ListCreateAPIView):
    queryset = Sku.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TransactionDetail(generics.RetrieveDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]


#Client
        
class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    @action(detail=True, methods=["get"])
    def getbyname(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(name=self.kwargs['name'])
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=ClientSerializer(client)
        return Response(serializer.data)
    


#Order
    
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class OrderDetail(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]