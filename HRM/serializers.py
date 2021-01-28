from rest_framework import serializers
from HRM.models import Users

class UsersSerializer(serializers.ModelSerializer):
    employee_id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    ranking = serializers.FloatField(required=False)

    class Meta:
         model = Users
         fields = '__all__'
