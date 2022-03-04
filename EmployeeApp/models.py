from django.db import model
# Create your models here.
class Departments(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=400)


class Employee(models.Model1):
    EmployeeId=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=300)
    Department=models.CharField(max_length=300)
