from django.db import models


class Employee(models.Model):
    
    class Meta:
        verbose_name_plural = "Emplyee's"

    Fname  = models.CharField(max_length=250)
    Minit  = models.CharField(max_length=250)
    Lname  = models.CharField(max_length=250)
    Bdate  = models.CharField(max_length=250)
    Address  = models.CharField(max_length=250)
    Sex  = models.CharField(max_length=250)
    Salary  = models.CharField(max_length=250)
    #ForeignKey
    Super_ssn  = models.ForeignKey("self", on_delete=models.CASCADE,blank=True,null=True)
    dno = models.ForeignKey("department.Dnumber", on_delete=models.CASCADE,blank=True,null=True)


class Ssn(models.Model):
    class Meta:
        verbose_name_plural = 'SSN'
    ssn  = models.IntegerField()

