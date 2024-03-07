from django.db import models
from datetime import datetime 

# Create your models here.

class Sku(models.Model):
    sku_code = models.CharField(max_length = 20) 
    vehicle_code = models.CharField(max_length = 20)
    gate_code = models.CharField(max_length = 10)
    amount = models.IntegerField(default=20)
    instock_time = models.DateTimeField(verbose_name=('In-stock date'),default=datetime.now())
    outstock_time= models.DateTimeField(verbose_name=('Out-stock date'), null=True, default=None)

    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return self.sku_code
    def is_in_stock(self):
        if self.outstock_time is None:
            return False 
        else:
            return True
        
class Client(models.Model):
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    mobile = models.CharField(max_length = 20)
    address = models.CharField(max_length = 50)

    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        
class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    deal_time= models.DateTimeField(default=datetime.now())
    
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

 
class Order(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    process_time= models.DateTimeField(verbose_name=('Order date'),default=datetime.now())
    status_code = models.CharField(max_length = 2)
    sku_code = models.CharField(max_length = 20)
    amount = models.IntegerField(default=1)

    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)



