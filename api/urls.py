from django.urls import path
from .views import *
app_name = 'api'

from rest_framework.urlpatterns import format_suffix_patterns

# from rest_framework import routers
# router = routers.DefaultRouter()

# router.register(r'custom_dron', CustomDronView, basename='available')

urlpatterns = [
    # path('dron', Dron_APIView.as_view()), 
    # path('dron/<int:pk>/', Dron_APIView_Detail.as_view()),
    # path('drug', Drug_APIView.as_view()), 
    # path('drug/<int:pk>/', Drug_APIView_Detail.as_view()),
    path('drons/', dron_list),
    path('drons/<int:pk>/', dron_detail),
    path('drugs/', drug_list),
    path('drugs/<int:pk>/', drug_detail),
    path('drons_status/', DronList.as_view()),
    path('drugs_dron/', DronDrugList.as_view()),
    path('batteryCapacity/', batteryCapacity),
    path('historial/', historial),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)