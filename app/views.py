from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
import json
from django.contrib import messages
from .models import Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'app/home.html', context)

def cart(request):
    account = request.user.acount
    cart = Cart.objects.all()
    items = Cart_Item.objects.all()
    context = {'items': items, 'cart': cart}
    return render(request, 'app/cart.html', context)

def checkout(request):
    account = request.user.acount
    cart = Cart.objects.all()
    items = Cart_Item.objects.all()
    context = {'items': items, 'cart': cart}
    return render(request, 'app/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    acount = request.user.acount
    product = Product.objects.get(id = productId)
    cart = Cart.objects.all()
    items = Cart_Item.objects.all()
    if action == 'add':
        Cart_Item.quantity += 1
    elif action == 'remote':
        Cart_Item.quantity -= 1
    Cart_Item.save()

def detail(request):
    idd = request.GET.get('id', '')
    products = Product.objects.filter(id = idd)
    context = {'products': products}
    return render(request, 'app/detail.html', context)
#dan
def product_list(request):
    items_product = Product.objects.all()
    search_query = request.GET.get('search_query')

    if search_query:
        items_product = Product.objects.filter(name__icontains=search_query)

    return render(request, 'app/product_list.html', {"items_product": items_product})

def product_create(request):
    if request.method == "POST":
        name = request.POST['name']
        deciption = request.POST['deciption']
        price = request.POST['price']
        image = request.FILES['image']  # Sử dụng request.FILES để lấy tệp hình ảnh
        item_product = Product(name=name, deciption=deciption, price=price, image=image)
        item_product.save()

        messages.success(request,'sản phẩm đã được tạo thành công!')
        return redirect('/list')  # Chuyển hướng tới trang danh sách sản phẩm sau khi tạo
    return render(request,'app/product_create.html',{})

def product_update(request, id):
    item_product = Product.objects.get(id=id)
    if request.method == "POST":
        item_product.name = request.POST['name']
        item_product.deciption = request.POST['deciption']
        item_product.price = request.POST['price']
        
        # Kiểm tra nếu người dùng đã chọn một tệp hình ảnh mới
        if 'image' in request.FILES:
            item_product.image = request.FILES['image']

        item_product.save()

        messages.success(request, 'Sản phẩm đã được cập nhật thành công!')
        return redirect('/list')  # Chuyển hướng tới trang danh sách sản phẩm sau khi cập nhật
    return render(request, 'app/product_update.html', {"item_product": item_product})
def product_delete(request, id):
    item_product = Product.objects.get(id=id)
    item_product.delete()
    messages.success(request, 'Sản phẩm đã được xoá thành công!')
    return redirect('/list')  # Chuyển hướng tới trang danh sách sản phẩm sau khi xoá