from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True, verbose_name='学号')
    name = models.CharField(max_length=50, verbose_name='姓名')
    college = models.CharField(max_length=100, verbose_name='学院')
    major = models.CharField(max_length=100, verbose_name='专业')
    class_name = models.CharField(max_length=50, verbose_name='班级')

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'

    def __str__(self):
        return self.name
