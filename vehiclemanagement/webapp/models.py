from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


    groups = models.ManyToManyField(
    'auth.Group',
    verbose_name='groups',
    blank=True,
    help_text='The groups this user belongs to.',
    related_name='webapp_user_set',  # Custom related_name
    related_query_name='user',
)
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='webapp_user_set',  # Custom related_name
        related_query_name='user',
    )



class Vehicle(models.Model):
    vehicle_number=models.CharField(max_length=50,unique=True)
    options=(
        ('two','two'),
        ('three','three'),
        ('four','four'),

    )
    vehicle_type=models.CharField(max_length=50,choices=options)
    vehicle_model=models.CharField(max_length=50,null=True)
    vehicle_description=models.TextField(max_length=500,null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    is_active=models.BooleanField(default=True,null=True)

    @property
    def get_img(self):
        img = VehicleImage.objects.filter(vehicle=self)
        print(img)
        return img
    
    def __str__(self):
        return self.vehicle_number
    

class VehicleImage(models.Model):
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True,related_name='image')
    image=models.ImageField(upload_to='vehicle_images',null=True,blank=True)

    def __str__(self):
        return self.vehicle.vehicle_number
    