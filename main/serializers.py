from main.models import User, Employee, Order, Payment, Report, Cassa, Garage, Occupation, Comment

from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'phone_number')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'user', 'address', 'occupation', 'garage', 'experience', 'wages', 'start_work_time', 'end_work_time', 'day_off', 'queue', 'qr_code', )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('code',)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ('code', )


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'employee', 'order', 'analysis_answer', 'things_done', 'total_cost', 'total_benefit', )


class CassaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = ('id', 'total_summa', )


class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = ('id', 'number', )


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ('id', 'name', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'order', 'type', 'create_at', )

