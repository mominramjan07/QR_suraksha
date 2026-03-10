from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100)
    insurance_number = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    medical_notes = models.TextField()
    family_name = models.CharField(max_length=100)
    family_phone = models.CharField(max_length=20)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    aadhar = models.FileField(upload_to='documents/', blank=True, null=True)
    rc_book = models.FileField(upload_to='documents/', blank=True, null=True)
    license = models.FileField(upload_to='documents/', blank=True, null=True)
    insurance = models.FileField(upload_to='documents/', blank=True, null=True)
    
    # New field for profile image
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return self.owner_name