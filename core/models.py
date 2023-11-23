from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_code=models.CharField(max_length=200,unique=True)
    name=models.CharField(max_length=200)
    contact=models.CharField(max_length=20)
    details=models.TextField( blank=True,null=True)
    address=models.TextField()

    def __str__(self):
        return f"{self.vendor_code} - {self.name}"




on_time_delivery_rate = models.FloatField(default=0.0)
quality_rating = models.FloatField(default=0.0)
response_time = models.DurationField(null=True, blank=True)
fulfilment_rate = models.FloatField(default=0.0)

    
class PurchaseOrder(models.Model):

    STATUS_CHOICES=[
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    ]
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    quality_rating = models.FloatField(default=0.0)
    response_time = models.DurationField(null=True, blank=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='Pending')
    promised_delivery_date = models.DateField(default='2023-01-01')
    fulfillment_rate = models.FloatField(default=0.0)
    actual_delivery_date = models.DateField(null=True, blank=True)

    def is_delivered_on_time(self):
        return self.status == 'Delivered' and self.actual_delivery_date <= self.promised_delivery_date

    def calculate_fulfillment_rate(self):
        total_orders = self.purchase_orders.count()
        fulfilled_orders = self.purchase_orders.filter(status='Delivered').count()

        if total_orders == 0:
            return 0.0

        return (fulfilled_orders / total_orders) * 100



class Purchase(models.Model):
    po_number=models.CharField(max_length=20,unique=True)
    Vendor_reference=models.CharField(max_length=50)
    order_date=models.DateField()
    items=models.TextField()
    quantity=models.PositiveIntegerField()

    
    STATUS_CHOICES=[
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    ]

    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='Pending')

    def __str__(self):
        return f"Purchase Order #{self.po_number}"