from django.db import models

class Todolist(models.Model):
	title = models.CharField(max_length=100)
	detail = models.TextField(null=True, blank=True) #null=True, blank=True คือไม่บังคับใส่

	def __str__(self):
		return self.title #เพื่อให้โชว์ title ในส่วนของหัวข้อ
