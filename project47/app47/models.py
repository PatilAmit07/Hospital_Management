from django.db import models
from django.db.models import CASCADE


# Create your models here.

class a1(models.Model):
    patient_id= models.CharField(max_length=10)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    treated_for=models.CharField(max_length=100)
    # date_admitted=models.DateField(max_length=30)
    prescription=models.CharField(max_length=100)
    prescription_type = models.CharField(max_length=100)
    # expected_sign_off=models.DateField(max_length=30)
    previous_history=models.CharField(max_length=100)
    emergency_contact=models.CharField(max_length=10)
    health_insurance=models.CharField(max_length=10)

class a2(models.Model):
    patient_id = models.ForeignKey(a1,on_delete=CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    prescription = models.CharField(max_length=100)
    emergency_contact = models.CharField(max_length=10)
    health_insurance = models.CharField(max_length=10)

