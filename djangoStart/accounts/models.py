from django.contrib.auth import decorators
from django.db import models
from django.contrib.auth.models import User

""" 

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name=models.CharField(max_length=200, null=True, blank=True)
    last_name=models.CharField(max_length=200,null=True, blank=True)
    phone=models.CharField(max_length=200, null=True,blank=True)

    def __str__(self) :
        return self.first_name

def create_profile():
        if created:
            Profile.objects.create(user=instance)
            print('profile created')


def update_profile(): 
    if created==False:
        print()
        try:
            instance.profile.save()
            print('profile updated')
        except:
            Profile.objects.create(user=instance)
            print('profile was created')"""



# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
class Customer(models.Model):
    user= models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name= models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200,null=True)
    date_created= models.DateTimeField(auto_now_add=True,null=True)
    profile_pic=models.ImageField(default="ikoo.png",null=True, blank=True)
    def __str__(self):
        return self.name+ ' '+ self.email



class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
        
    )
    name=models.CharField(max_length=200, null=True)
    price=models.CharField(max_length=200, null=True)
    category=models.CharField(max_length=200, null=True, choices=CATEGORY)
    description=models.CharField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return self.name
class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )

    customer=models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product=models.ForeignKey(Product, null= True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=200, null=True,choices=STATUS)
    note=models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.product.name