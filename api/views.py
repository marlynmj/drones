from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DronSerializer, DrugSerializer, HistorialSerializer
from .models import Dron, Drug, Historial
from rest_framework import status, generics
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

class DronList(generics.ListAPIView):
    serializer_class = DronSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Dron.objects.all()
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset

class DronDrugList(generics.ListAPIView):
    serializer_class = DrugSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Drug.objects.all()
        dron = self.request.query_params.get('dron')
        if dron is not None:
            queryset = queryset.filter(dron=dron)
        return queryset

@api_view(['GET'])
def batteryCapacity(request):
    serialNumber = request.query_params.get('serialNumber')
    if serialNumber is not None:
        dron = Dron.objects.get(serialNumber=serialNumber)
        serializer = DronSerializer(dron)
        return Response({'batteryCapacity': serializer.data['batteryCapacity']})

# from rest_framework import viewsets

# class CustomDronView(viewsets.ViewSet):
#     def list(self, request, format=None):
#         drons = [dron.dron_text for dron 
#         in Dron.objects.filter(status='id')]
#         return Response(drons)

# class DronList(generics.ListAPIView):
#     serializer_class = DronSerializers

#     def get_queryset(self):
#         queryset = Dron.objects.all()
#         serialNumber = self.request.query_params.get('serialNumber')
#         if serialNumber is not None:
#             queryset = queryset.filter(serialNumber=serialNumber)
#         return queryset

# from .filters import DronFilter
@api_view(['GET', 'POST'])
def dron_list(request, format=None):
    """
    List all code drons, or create a new dron.
    """
    if request.method == 'GET':
        # queryset = Dron.objects.all()
        # filterset = DronFilter(request.GET, queryset=queryset)
        # if filterset.is_valid():
        #     queryset = filterset.qs
        # serializer = DronSerializer(queryset, many=True)
        # return Response(serializer.data)
    #-----------------------------------------
        drons = Dron.objects.all()
        serializer = DronSerializer(drons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DronSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def dron_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code dron.
    """
    try:
        dron = Dron.objects.get(pk=pk)
    except Dron.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DronSerializer(dron)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DronSerializer(dron, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dron.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class Dron_APIView(APIView):   
#     def get(self, request, format=None, *args, **kwargs):
#         dron = Dron.objects.all()
#         serializer = DronSerializer(dron, many=True)
        
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = DronSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def list(self, request, format=None):
    #     dron = Dron.objects.filter(status='id')
    #     serializer = DronSerializers(dron, many=True)
        
    #     return Response(serializer.data)


# class Dron_APIView_Detail(APIView):

#     def get_object(self, pk):
#         try:
#             return Dron.objects.get(pk=pk)
#         except Dron.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         Dron = self.get_object(pk)
#         serializer = DronSerializer(Dron)  
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         dron = self.get_object(pk)
#         serializer = DronSerializer(dron, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         dron = self.get_object(pk)
#         dron.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def drug_list(request):
    """
    List all code drugs, or create a new drug.
    """
    if request.method == 'GET':
        drugs = Drug.objects.all()
        serializer = DrugSerializer(drugs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DrugSerializer(data=request.data)
        if serializer.is_valid():
            #---weightLimit|batteryCapacity---
            dron = Dron.objects.get(pk=request.data['dron'])
            if (float(dron.weightLimit) >= float(request.data['weight'])) and (dron.batteryCapacity > 25):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def drug_detail(request, pk):
    """
    Retrieve, update or delete a code drug.
    """
    try:
        drug = Drug.objects.get(pk=pk)
    except Drug.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DrugSerializer(drug)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrugSerializer(drug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class Drug_APIView(APIView):   
#     def get(self, request, format=None, *args, **kwargs):
#         drug = Drug.objects.all()
#         serializer = DrugSerializer(drug, many=True)
        
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = DrugSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Drug_APIView_Detail(APIView):

#     def get_object(self, pk):
#         try:
#             return Drug.objects.get(pk=pk)
#         except Drug.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         Drug = self.get_object(pk)
#         serializer = DrugSerializer(Drug)  
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         drug = self.get_object(pk)
#         serializer = DrugSerializer(drug, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         drug = self.get_object(pk)
#         drug.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def historial(request, format=None):
    if request.method == 'GET':
        histo = Historial.objects.all()
        serializer = HistorialSerializer(histo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HistorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)