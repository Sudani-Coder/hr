from django.db import models


class DependentName(models.Model):
    class Meta:
        # db_table = 'dependent_name'
        verbose_name_plural = 'Dependent Name'
    
    Sex  =  models.CharField(max_length=250)
    Bdate  =  models.CharField(max_length=250)
    Relationship =  models.CharField(max_length=250)
    # Primary_key
    Dependent_name  =  models.CharField(primary_key=True, max_length=250)
    # ForienKey
    Essn  =  models.ForeignKey("employee.Employee", on_delete=models.CASCADE)
    