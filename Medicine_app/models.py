from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from datetime import date

# Create your models here.
class Signup(models.Model): 
    username = models.CharField(max_length=255,)
    password = models.CharField(max_length=128, validators=[MinLengthValidator(8)])
    email = models.EmailField()
    m_no = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{10}$', message='Mobile number must be exactly 10 digits')])
    dob = models.DateField(default=date.today)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])


    def calculate_age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def save(self, *args, **kwargs):
        self.age = self.calculate_age()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.password
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()

    def __str__(self):
        return self.name