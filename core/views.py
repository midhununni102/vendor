from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import Vendor,Purchase
from core.serializers import VendorSerializer,PurchaseOrderSerializer,VendorPerformanceSerializer
# Create your views here.
class VendorListCreateView(generics.ListCreateAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Vendor.objects.all()
    serializer_class=   VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset=Purchase.objects.all()
    serializer_class=PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Purchase.objects.all()
    serializer_class=PurchaseOrderSerializer

class VendorPerformanceView(APIView):
    def get(self, request, pk):
        try:
            vendor = Vendor.objects.get(pk=pk)
            serializer = VendorPerformanceSerializer(vendor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)