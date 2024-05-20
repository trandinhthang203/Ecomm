from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import make_password

class Account(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('locked', 'Locked'),
    )
    id = models.AutoField(primary_key=True)  
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')  # Sử dụng default để gán giá trị mặc định

    def save(self, *args, **kwargs):
        # Mã hóa mật khẩu trước khi lưu vào cơ sở dữ liệu
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    
class DetailAccount(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    id_account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='detail')
    def __str__(self) :
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    deciption = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self) :
        return self.name
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Bill(models.Model):
    Account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)

class Bill_Detail(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    total_price = models.CharField(max_length=200, null=True)

    
class Cart(models.Model):
    Account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return str(self.id)

class Cart_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=False)
    quantity = models.IntegerField(default=0, null=True, blank=True)

