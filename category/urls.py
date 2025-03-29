from django.urls import path
from . import views

urlpatterns = [
    path("",views.first_category,name='first_option'),
    path("electricity/",views.electricity_views,name='electricity_name'),
    path("recharge/",views.recharge_views,name='recharge_name'),
    path("insurance/",views.insurance_views,name='insurance_name'),
    path("pan/",views.pan_views,name='pan_name'),
    path("topup/",views.topup_views,name='topup_name'),
    path("travel/",views.travel_views,name='travel_name'),
    path("esevai/",views.esevai_views,name='esevai_name'),
    path("bank/",views.bank_views,name='bank_name'),
    path("enrollment/",views.enrollment_views,name='enrollment_name'),
]
