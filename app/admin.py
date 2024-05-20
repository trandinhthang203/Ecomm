from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Account)
admin.site.register(DetailAccount)
admin.site.register(Cart)
admin.site.register(Cart_Item)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Bill_Detail)