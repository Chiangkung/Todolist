from django.contrib import admin
from .models import Todolist

admin.site.register(Todolist) #ทำให้ model นี้อยู่ในฝั่งที่เป็น admin
