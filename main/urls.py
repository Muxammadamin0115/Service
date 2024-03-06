from django.urls import path
from .views import *

urlpatterns = [
    #"""""Start filter and get Employee Model"""""
    path('filter-employees-by-user-age/', filter_employees_by_user_age_view),
    path('filter-employees-by-occupation-name/', filter_employees_by_occupation_name_view),
    path('filter-employees-by-experience/', filter_employees_by_experience_view),
    path('filter-employees-by-wages/', filter_employees_by_wages_view),
    path('filter-employees-by-start-work-time/', filter_employees_by_start_work_time_view),
    path('filter-employees-by-end-work-time/', filter_employees_by_end_work_time_view),
    path('filter-employees-by-start-work-time-and-end-work-time/', filter_employees_by_start_work_time_and_end_work_time_view),
    path('filter-employees-by-days-off/', filter_employees_by_days_off_view),
    path('filter-employees-day-off/', filter_employees_day_off_view),
    path('filter-employees-by-queue/', filter_employees_by_queue_view),
    path('get-employee-by-user-username/', get_employee_by_user_username_view),
    path('get-employee-by-user-phone-number/', get_employee_by_user_phone_number_view),
    path('get-employee-by-user-email/', get_employee_by_user_email_view),
    path('get-employee-by-user-garage/', get_employee_by_user_garage_view),
    #"""""End filter and get Employee Model"""""

    #"""""Start filter and get Order Model"""""
    path('filter-orders-by-employee-user-username/', filter_orders_by_employee_user_username_view),
    path('filter-orders-by-employee-occupation-name/', filter_orders_by_employee_occupation_name_view),
    path('filter-orders-by-employee-garage-number/', filter_orders_by_employee_garage_number_view),
    path('filter-orders-by-owner-name/', filter_orders_by_owner_name_view),
    path('filter-orders-by-owner-phone-number/', filter_orders_by_owner_phone_number_view),
    path('filter-orders-by-owner-car-number/', filter_orders_by_owner_car_number_view),
    path('filter-orders-by-car-passport-number/', filter_orders_by_car_passport_number_view),
    path('filter-orders-by-status/', filter_orders_by_status_view),
    path('get-order-by-code/', get_order_by_code_view),
    #"""""End filter and get Order Model"""""

    #"""""Start get and filter Payment Model"""""
    path('get-payment-by-order/', get_payment_by_order_view),
    path('get-payment-by-code/', get_payment_by_code_view),
    path('filter-payment-by-payment/', filter_payment_by_payment_view),
    path('filter-payment-by-payment-type/', filter_payment_by_payment_type_view),
    #"""""End get and filter Payment Model"""""

    #"""""Start get and filter Report Model"""""
    path('get-report-by-order/', get_report_by_order_view),
    path('filter-report-by-employee/', filter_report_by_employee_view),
    #"" """End get and filter Report Model"""""

    #"""""Start filter Comment Model"""""
    path('filter-comment-by-type/', filter_comment_by_type_view),
    #"""""End filter Comment Model"""""
]