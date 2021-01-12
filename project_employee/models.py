from django.db import models


class ProjectEmployee(models.Model):
    ''' I've changed the project model ==> ProjectEmployee'''

    class Meta:
        # db_table = 'project' # project_employee table name
        verbose_name_plural = 'Project Employee'
        
    Pname  = models.CharField(max_length=250)
    Plocation  = models.CharField(max_length=250)
    #Primary_key
    pnumber  = models.AutoField(primary_key=True)
    #ForeignKey
    Dnum = models.ForeignKey("department.Department",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Pname
    
