# serializers.py

from rest_framework import serializers
from .models import Todolist

class TodolistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todolist
		fields = ('id','title','detail') #'__all__' สามารถใส่คำนี้แทนได้ถ้าต้องการให้ save ได้ทุก details