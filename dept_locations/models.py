from django.db import models

class DeptLocations(models.Model):
    class Meta:
        # db_table = 'dept_locations'
        verbose_name_plural = 'Depts Locations'


    Dlocation = models.CharField(primary_key=True,max_length=250)
    #ForeignKey
    Dnumber = models.ForeignKey('department.Department', on_delete=models.CASCADE)