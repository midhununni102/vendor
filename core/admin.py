from django.contrib import admin
from core.models import Vendor,Purchase,PurchaseOrder
# Register your models here.
admin.site.register(Vendor)
admin.site.register(Purchase)
admin.site.register(PurchaseOrder)