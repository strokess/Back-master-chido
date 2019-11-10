from django.db import models
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    calle = models.CharField(max_length=15)
    colonia = models.CharField(max_length=15)
    municipio = models.CharField(max_length=15)
    numeroE = models.CharField(max_length=15)
    numeroI = models.CharField(max_length=15)
    cp= models.CharField(max_length = 6)
    periodicidad = models.CharField(max_length=10)
    class Meta:
        db_table = "employee"

