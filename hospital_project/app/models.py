from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    medical_history = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.age} years old) - {self.gender} - {self.email}"