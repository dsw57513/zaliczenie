from django.shortcuts import render
from order_display.models import Order, Element
from django.contrib.auth.models import User 
# Create your views here.

def order_list(request):
    worker = request.user
    orders = Order.objects.filter(workers = worker)
    return render(request, 'worker_app/order_list.html', {'orders':orders})

def order_detail(request, order):
    order = Order.objects.get(slug = order)
    elements = order.element.all()
    return render(request, 'worker_app/order_detail.html', {'order':order, 'elements':elements})