from django.urls import path
from .views import *


urlpatterns = [
    #""""" Start CRUD Employee Urls"""
    path('create-employee-api/', Create_Employee_Api_View.as_view()),
    path('get-employee-items/', Get_All_Employee_Items.as_view()),
    path('update-employee-api/<int:pk>/', Update_Employee_Api_View.as_view()),
    path('delete-employee-api/<int:pk>/', Delete_Employee_Api_View.as_view()),
    #""""" End CRUD Employee Urls"""

    #""""" Start CRUD Order Urls"""
    path('create-order-api/', Create_Order_Api_View.as_view()),
    path('get-order-items/', Get_All_Order_Items.as_view()),
    path('update-order-api/<int:pk>/', Update_Order_Api_View.as_view()),
    path('delete-order-api/<int:pk>/', Delete_Order_Api_View.as_view()),
    #""""" End CRUD Order Urls"""

    #""""" Start CRUD Payment Urls"""
    path('create-payment-api/', Create_Payment_Api_View.as_view()),
    path('get-payment-items/', Get_All_Payment_Items.as_view()),
    path('update-payment-api/<int:pk>/', Update_Payment_Api_View.as_view()),
    path('delete-payment-api/<int:pk>/', Delete_Payment_Api_View.as_view()),
    #""""" End CRUD Payment Urls"""

    #""""" Start CRUD Report Urls"""
    path('create-report-api/', Create_Report_Api_View.as_view()),
    path('get-report-items/', Get_All_Report_Items.as_view()),
    path('update-report-api/<int:pk>/', Update_Report_Api_View.as_view()),
    path('delete-report-api/<int:pk>/', Delete_Report_Api_View.as_view()),
    #""""" End CRUD Report Urls"""

    #""""" Start CRUD Cassa Urls"""
    path('create-cassa-api/', Create_Cassa_Api_View.as_view()),
    path('get-cassa-items/', Get_All_Cassa_Items.as_view()),
    path('update-cassa-api/<int:pk>/', Update_Cassa_Api_View.as_view()),
    path('delete-cassa-api/<int:pk>/', Delete_Cassa_Api_View.as_view()),
    #""""" End CRUD Cassa Urls"""

    #""""" Start CRUD Garage Urls"""
    path('create-garage-api/', Create_Garage_Api_View.as_view()),
    path('get-garage-items/', Get_All_Garage_Items.as_view()),
    path('update-garage-api/<int:pk>/', Update_Garage_Api_View.as_view()),
    path('delete-garage-api/<int:pk>/', Delete_Garage_Api_View.as_view()),
    #""""" End CRUD Garage Urls"""

    #""""" Start CRUD Occupation Urls"""
    path('create-occupation-api/', Create_Occupation_Api_View.as_view()),
    path('get-occupation-items/', Get_All_Occupation_Items.as_view()),
    path('update-occupation-api/<int:pk>/', Update_Occupation_Api_View.as_view()),
    path('delete-occupation-api/<int:pk>/', Delete_Occupation_Api_View.as_view()),
    #""""" End CRUD Occupation Urls"""

    # """"" Start CRUD Comment Urls"""
    path('create-comment-api/', Create_Comment_Api_View.as_view()),
    path('get-comment-items/', Get_All_Comment_Items.as_view()),
    path('update-comment-api/<int:pk>/', Update_Comment_Api_View.as_view()),
    path('delete-comment-api/<int:pk>/', Delete_Comment_Api_View.as_view()),
    # """"" End CRUD Comment Urls"""
]