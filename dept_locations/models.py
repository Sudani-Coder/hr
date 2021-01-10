from django.db import models

class DeptLocations(models.Model):
    class Meta:
        verbose_name_plural = 'Depts Locations'

    Dlocation = models.CharField(max_length=250)

    #ForeignKey
    Dnumber = models.ForeignKey("department.Dnumber", on_delete=models.CASCADE)