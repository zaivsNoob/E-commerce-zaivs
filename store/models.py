from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=200,null='true',blank='true')
    price=models.FloatField(null='true')
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    user=models.OneToOneField(User,null='true',on_delete=models.CASCADE,blank='true')
    name=models.CharField(max_length=200,null='true',blank='true')
    email=models.CharField(max_length=200,null='true',blank='true')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer=models.ForeignKey(Customer,null='true',on_delete=models.SET_NULL,blank='true')
    date_ordered=models.DateTimeField(auto_now_add='true')
    transaction_id=models.CharField(max_length=200,null='true',blank='true')
    completed=models.BooleanField(null='true')
    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product=models.ForeignKey(Product,null='true',on_delete=models.SET_NULL,blank='true') 
    order=models.ForeignKey(Order,null='true',on_delete=models.SET_NULL,blank='true')
    date_ordered=models.DateTimeField(auto_now_add='true') 
    quantity=models.IntegerField(default=0,null='true',blank='true')   

    def __str__(self):
        return str(self.id)
    def get_total(self):
        if self.product:
            return self.product.price * self.quantity
        return 0

class ShippingAdress(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,null='true',blank='true')
    order=models.OneToOneField(Order,null='true',on_delete=models.CASCADE,blank='true')
    address=models.CharField(max_length=200,null='true',blank='true')

    def __str__(self):
        return self.address