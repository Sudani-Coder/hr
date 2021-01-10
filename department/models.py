from django.db import models


class Department(models.Model):
    class Meta:
        verbose_name_plural = 'Department'

    Dname  = models.CharField(max_length=250)
    Mgr_ssn  = models.CharField(max_length=250)
    Mgr_start_date = models.CharField(max_length=250)


class Dnumber(models.Model):
    dnumber  = models.IntegerField()