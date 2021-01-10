from django.db import models


class WorksOn(models.Model):
    class Meta:
        verbose_name_plural = "Works On"

    Hours = models.CharField(max_length=250)
    
    #forignkey 
    Pno  = models.ForeignKey("project_employee.Pnumber",on_delete=models.CASCADE)
    Essn  = models.ForeignKey("employee.Ssn",on_delete=models.CASCADE)