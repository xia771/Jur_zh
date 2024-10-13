from django.shortcuts import render, redirect

from .forms import ProductForm, OrderForm
from shoppapp.models import Product


def index(request):
    return render(request,'base.html')
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request,'product_list.html',{'products':products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            # 使用无效的表单重新渲染页面，以便显示错误信息
            return render(request, 'add.html', {'form': form})
    else:
        form = ProductForm()
        return render(request, 'add.html', {'form': form})

def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request,'edit.html',{'form':form})


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete.html', {'product': product})

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    # 实现添加到购物车的逻辑
    return redirect('product_list')

def cart(request):
    # 展示购物车内容的逻辑
    return render(request, 'cart.html')

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            # 计算总价等逻辑
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})