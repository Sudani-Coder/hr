from django.db import models


class DependentName(models.Model):
    class Meta:
        verbose_name_plural = 'Dependent Name'
    
    Dependent_name  =  models.CharField(max_length=250)
    Sex  =  models.CharField(max_length=250)
    Bdate  =  models.CharField(max_length=250)
    Relationship =  models.CharField(max_length=250)
    # ForienKey
    Essn  =  models.ForeignKey("employee.Ssn", on_delete=models.CASCADE)
    