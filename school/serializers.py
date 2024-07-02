from rest_framework import serializers
from .models import *


class studentSerailizer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields="__all__"


class SchoolSerializer(serializers.ModelSerializer):
    Student=studentSerailizer(many=True,read_only=True)
    class Meta:
        model=school
        fields="__all__"