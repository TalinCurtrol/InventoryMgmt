from rest_framework import serializers
from store.models import Sku,Client,Order,Transaction
from django.contrib.auth.models import User
class SkuSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Sku
        fields = ['id','sku_code','vehicle_code','gate_code','instock_time','outstock_time','owner']

    def create(self, validated_data):
        return Sku.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.sku_code = validated_data.get('sku_code', instance.sku_code)
        instance.vehicle_code = validated_data.get('vehicle_code', instance.vehicle_code)
        instance.gate_code = validated_data.get('gate_code', instance.gate_code)
        instance.order_code = validated_data.get('order_code', instance.order_code)
        instance.instock_time = validated_data.get('instock_time', instance.instock_time)
        instance.outstock_time = validated_data.get('outstock_time', instance.outstock_time)
        instance.save()
        return instance
    


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ['id', 'username']

class ClientSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Client
        fields = ['id', 'name','email','mobile','address','owner']

    def create(self, validated_data):
        return Client.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
    

class TransactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    client = serializers.ReadOnlyField(source='client.id')
    class Meta:
        model = Transaction
        fields = ['id', 'client','deal_time','owner']

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Order
        fields = ['id', 'transaction','process_time','status_code','sku_code','amount','owner']

    def create(self, validated_data):
        return Order.objects.create(**validated_data)