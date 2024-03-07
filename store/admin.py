from django.contrib import admin

from .models import Sku,Client,Order,Transaction

admin.site.register(Sku)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Transaction)