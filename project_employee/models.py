from django.db import models


class ProjectEmployee(models.Model):
    ''' I've changed the project model ==> ProjectEmployee'''

    class Meta:
        verbose_name_plural = 'Project Employee'
        
    Pname  = models.CharField(max_length=250)
    Plocation  = models.CharField(max_length=250)
    #ForeignKey
    Dnum = models.ForeignKey("department.Dnumber",on_delete=models.CASCADE)

class Pnumber(models.Model):
    pnumber  = models.CharField(max_length=250)