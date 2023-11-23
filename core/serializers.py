from rest_framework import serializers
from core.models import Vendor,Purchase,PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'vendor_code', 'name', 'contact', 'details', 'address']
        read_only_fields = ['id']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purchase
        fields= ['quality_rating', 'response_time', 'status']

class VendorPerformanceSerializer(serializers.ModelSerializer):
    Purchase_order=PurchaseOrderSerializer(many=True,read_only=True)
    
    class Meta:
        model=Vendor
        fields = ['on_time_delivery_rate', 'quality_rating', 'response_time', 'fulfilment_rate', 'purchase_orders']
