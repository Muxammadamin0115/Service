from main.models import *
from main.serializers import *
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response

#"""""Start filter and get Employee Model"""""
# start filter Employees.user.age
@api_view(['GET'])
def filter_employees_by_user_age_view(request):
    small_age = int(request.GET.get('small_age'))
    large_age =int(request.GET.get('large_age'))
    if small_age > 17 and large_age > 17:
        employees = User.objects.filter(age__gte=small_age, age__lte=large_age)
        if employees:
            ser = UserSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    else:
            message = 'Workers under the age of 18 are not accepted'
            return Response(message)

# end filter Employees.user.age

# start filter Employees.occupation.name
@api_view(['GET'])
def filter_employees_by_occupation_name_view(request):
    name = request.GET['name']
    try:
        employees = Employee.objects.filter(occupation__name=name)
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Employees.occupation.name

# start filter Employees.experience
@api_view(['GET'])
def filter_employees_by_experience_view(request):
    small_experience = request.GET.get('small_experience')
    large_experience = request.GET.get('large_experience')
    try:
        employees = Employee.objects.filter(experience__gte=small_experience, experience__lte=large_experience)
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# start filter Employees.experience

# start filter Employees.wages
@api_view(['GET'])
def filter_employees_by_wages_view(request):
    small_wages = request.GET.get('small_wages')
    large_wages = request.GET.get('large_wages')
    try:
        employees = Employee.objects.filter(wages__gte=small_wages, wages__lte=large_wages)
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# start filter Employees.wages

# start filter Employees.start_work_time
@api_view(['GET'])
def filter_employees_by_start_work_time_view(request):
    small_start_work_time = request.GET.get('small_start_work_time')
    large_start_work_time = request.GET.get('large_start_work_time')
    print(small_start_work_time, large_start_work_time)
    try:
        employees = Employee.objects.filter(start_work_time__gte=small_start_work_time, start_work_time__lte=large_start_work_time)
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# start filter Employees.start_work_time

# start filter Employees.end_work_time
@api_view(['GET'])
def filter_employees_by_end_work_time_view(request):
    small_end_work_time = request.GET.get('small_end_work_time')
    large_end_work_time = request.GET.get('large_end_work_time')
    try:
        employees = Employee.objects.filter(end_work_time__gte=small_end_work_time, end_work_time__lte=large_end_work_time)
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# start filter Employees.end_work_time

# start filter Employees.start_work_time and end_work_time
@api_view(['GET'])
def filter_employees_by_start_work_time_and_end_work_time_view(request):
    start_work_time = request.GET.get('start_work_time')
    end_work_time = request.GET.get('end_work_time')
    try:
        employees = Employee.objects.filter(start_work_time__gte=start_work_time, end_work_time__lte=end_work_time)
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Employees.start_work_time and end_work_time


# start filter Employees.days_off
@api_view(['GET'])
def filter_employees_by_days_off_view(request):
    small_day_off = request.GET.get('small_day_off')
    large_day_off = request.GET.get('large_day_off')
    try:
        employees = Employee.objects.filter(day_off__gte=small_day_off, day_off__lte=large_day_off)
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Employees.days_off

# start filter Employees.day_off
@api_view(['GET'])
def filter_employees_day_off_view(request):
    day_off = request.GET['day_off']
    try:
        employees = Employee.objects.filter(day_off=day_off)
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Employees.day_off

# start filter Employee.queue
@api_view(['GET'])
def filter_employees_by_queue_view(request):
    small_queue = request.GET.get('small_queue')
    large_queue = request.GET.get('large_queue')
    try:
        employees = Employee.objects.filter(queue__gte=small_queue, queue__lte=large_queue)
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Employees.queue

# start get Employee.user.username
@api_view(['GET'])
def get_employee_by_user_username_view(request):
    username = request.GET['username']
    try:
        employee = User.objects.get(username=username)
        if employee:
            ser = UserSerializer(employee)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end get Employee.user.username

#""""Error +"""
# start get Employee.user.phone_number
@api_view(['GET'])
def get_employee_by_user_phone_number_view(request):
    phone_number = request.GET['phone_number']
    phone_number = '+' + phone_number
    print(phone_number)
    try:
        employee = Employee.objects.get(user__phone_number=phone_number)
        if employee:
            ser = EmployeeSerializer(employee)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end get Employee.user.phone_number

# start get Employee.user.email
@api_view(['GET'])
def get_employee_by_user_email_view(request):
    email = request.GET['email']
    try:
        employee = Employee.objects.get(user__email=email)
        if employee:
            ser = EmployeeSerializer(employee)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end get Employee.user.email

# start get Employee.garage
@api_view(['GET'])
def get_employee_by_user_garage_view(request):
    garage = request.GET['garage']
    try:
        employee = Employee.objects.get(garage=garage)
        if employee:
            ser = EmployeeSerializer(employee)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end get Employee.garage
#"""""End filter and get Employee Model"""""

#"""""Start filter and get Order Model"""""
# start filter Orders.employee.user.username
@api_view(['GET'])
def filter_orders_by_employee_user_username_view(request):
    username = request.GET['username']
    try:
        orders = Order.objects.filter(employee__user__username=username).order_by('-id')
        if orders:
            ser = OrderSerializer(orders, many=True)
            return Response(ser.data)
        else:
            message = 'No such order found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such order found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Orders.employee.user.username

# start filter Orders.employee.occupation.name
@api_view(['GET'])
def filter_orders_by_employee_occupation_name_view(request):
    name = request.GET['name']
    try:
        orders = Order.objects.filter(employee__occupation__name=name).order_by('-id')
        if orders:
            ser = OrderSerializer(orders, many=True)
            return Response(ser.data)
        else:
            message = 'No such order found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such order found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Orders.employee.occupation.name

# start filter Orders.employee.garage.number
@api_view(['GET'])
def filter_orders_by_employee_garage_number_view(request):
    number = request.GET['number']
    try:
        orders = Order.objects.filter(employee__garage__number=number).order_by('-id')
        if orders:
            ser = OrderSerializer(orders, many=True)
            return Response(ser.data)
        else:
            message = 'No such order found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such order found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Orders.employee.garage.number

# start filter Orders.owner_name
@api_view(['GET'])
def filter_orders_by_owner_name_view(request):
    owner_name = request.GET['owner_name']
    try:
        orders = Order.objects.filter(owner_name=owner_name).order_by('-id')
        if orders:
            ser = OrderSerializer(orders, many=True)
            return Response(ser.data)
        else:
            message = 'No such order found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such order found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Orders.owner_name

# start filter Orders.owner_phone_number
@api_view(['GET'])
def filter_orders_by_owner_phone_number_view(request):
    owner_phone_number = request.GET['owner_phone_number']
    owner_phone_number = '+' + owner_phone_number
    try:
        orders = Order.objects.filter(owner_phone_number=owner_phone_number).order_by('-id')
        if orders:
            ser = OrderSerializer(orders, many=True)
            return Response(ser.data)
        else:
            message = 'No such order found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such order found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Orders.owner_phone_number

# start filter Orders.owner_car_number
@api_view(['GET'])
def filter_orders_by_owner_car_number_view(request):
    owner_car_number = request.GET['owner_car_number']
    try:
        orders = Order.objects.filter(owner_car_number=owner_car_number).order_by('-id')
        if orders:
            ser = OrderSerializer(orders, many=True)
            return Response(ser.data)
        else:
            message = 'No such order found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such order found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Orders.owner_car_number

# start filter Orders.car_passport_number
@api_view(['GET'])
def filter_orders_by_car_passport_number_view(request):
    car_passport_number = request.GET['car_passport_number']
    try:
        orders = Order.objects.filter(car_passport_number=car_passport_number).order_by('-id')
        if orders:
            ser = OrderSerializer(orders, many=True)
            return Response(ser.data)
        else:
            message = 'No such order found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such order found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Orders.car_passport_number

# start filter Orders.status
@api_view(['GET'])
def filter_orders_by_status_view(request):
    status = request.GET['status']
    try:
        orders = Order.objects.filter(status=status).order_by('-id')
        if orders:
            ser = OrderSerializer(orders, many=True)
            return Response(ser.data)
        else:
            message = 'No such order found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such order found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Orders.status

# start get Order.code
@api_view(['GET'])
def get_order_by_code_view(request):
    code = request.GET['code']
    try:
        order = Order.objects.filter(code=code)
        if order:
            ser = OrderSerializer(order)
            return Response(ser.data)
        else:
            message = 'No such order found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such order found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end get Orders.code
#"""""End filter and get Order Model"""""

#"""""Start get and filter Payment Model"""""
#start get Payment.order
@api_view(['GET'])
def get_payment_by_order_view(request):
    order = request.GET['order']
    try:
        order = Payment.objects.filter(order=order)
        if order:
            ser = PaymentSerializer(order)
            return Response(ser.data)
        else:
            message = 'No such payment found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such payment found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end get Payment.order

#start get Payment.code
@api_view(['GET'])
def get_payment_by_code_view(request):
    code = request.GET['code']
    try:
        order = Payment.objects.filter(code=code)
        if order:
            ser = PaymentSerializer(order)
            return Response(ser.data)
        else:
            message = 'No such payment found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such payment found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end get Payment.code

#start filter Payment.payment
@api_view(['GET'])
def filter_payment_by_payment_view(request):
    small_amount = request.GET['small_amount']
    large_amount = request.GET['large_amount']
    try:
        payments = Payment.objects.filter(payment__gte=small_amount, payment__lte=large_amount).order_by('-id')
        if payments:
            ser = PaymentSerializer(payments, many=True)
            return Response(ser.data)
        else:
            message = 'No such payment found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such payment found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
#end filter Payment.payment

# start filter Payment.payment_type
@api_view(['GET'])
def filter_payment_by_payment_type_view(request):
    payment_type = request.GET['payment_type']
    try:
        payments = Payment.objects.filter(payment_type=payment_type).order_by('-id')
        if payments:
            ser = PaymentSerializer(payments, many=True)
            return Response(ser.data)
        else:
            message = 'No such payment found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such payment found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Payment.payment_type
#"""""End get and filter Payment Model"""""

#"""""Start get and filter Report Model"""""
# start get Report.order
@api_view(['GET'])
def get_report_by_order_view(request):
    order = request.GET['order']
    try:
        report = Report.objects.get(order=order)
        if report:
            ser = ReportSerializer(report)
            return Response(ser.data)
        else:
            message = 'No such report found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such report found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end get Report.order

# start filter Report.employee
@api_view(['GET'])
def filter_report_by_employee_view(request):
    employee = request.GET['employee']
    try:
        report = Report.objects.filter(employee=employee).order_by('-id')
        if report:
            ser = ReportSerializer(report, many=True)
            return Response(ser.data)
        else:
            message = 'No such report found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such report found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Report.employee
#"""""End get and filter Report Model"""""

#"""""Start filter Comment Model"""""
# start filter Comment.type
@api_view(['GET'])
def filter_comment_by_type_view(request):
    type = request.GET['type']
    try:
        comments = Comment.objects.filter(type=type).order_by('-id')
        if comments:
            ser = CommentSerializer(comments, many=True)
            return Response(ser.data)
        else:
            message = 'No such comment found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such comment found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Comment.type
#"""""End filter Comment Model"""""