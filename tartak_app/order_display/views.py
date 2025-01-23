from django.shortcuts import render, redirect, HttpResponse
from .models import Element, Order, Client
from .forms import ElementForm, OrderForm, ClientForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q


class OrderListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    queryset = Order.published.all()
    context_object_name = 'orders'
    template_name = 'order_display/order_list.html'

@login_required(login_url='/login/')   
def order_detail_view(request, order):
    order = Order.objects.get(slug=order)
    elements = order.element.all().order_by('status')
    if request.method == "POST":
        if 'element_form' in request.POST:
            element_form = ElementForm(request.POST)
            order_form = OrderForm()
            if element_form.is_valid():
                element = element_form.save(commit=False)
                element.order = order
                element.save()
        if 'order_form' in request.POST:
            order_form = OrderForm(request.POST, instance = order)
            element_form = ElementForm()
            if order_form.is_valid():
                order = order_form.save()
        return redirect(order.get_absolute_url())
    else:
        element_form = ElementForm()
        order_form=OrderForm(instance = order)
        

    return render(request, 'order_display/order_detail.html', {"order":order,"elements":elements, "element_form": element_form,'order_form':order_form})
    
@login_required(login_url='/login/')
def client_detail_view(request, client):
    client = Client.objects.get(slug = client)
    orders = client.order.all()
    return render(request, 'order_display/client.html', context={"client":client, "orders": orders})

@login_required(login_url='/login/')
def element_edit_view(request, element):
    element = Element.objects.get(slug = element)
    if request.method=='POST':
        element_form = ElementForm(request.POST, instance=element)
        if element_form.is_valid():
            element.save()
            return redirect(element.order.get_absolute_url())
    else:
        element_form = ElementForm(instance=element)
        
    return render(request, 'order_display/element_edit.html', {'element_form': element_form})


def new_order(request):
    if request.method=='POST':
        form = OrderForm(request.POST)
        client_form = ClientForm(request.POST)
        if form.is_valid() and client_form.is_valid():
            messages.success(request, "utworzono nowe zamówienie")
            order = form.save(commit=False)
            client = client_form.save(commit=False)
            if client.first_name or client.last_name or client.phone_number:
                exists = Client.objects.filter(first_name = client.first_name).filter(last_name=client.last_name)
                if exists:
                    order.client = exists[0]
                else:
                    client.save()
                    order.client = client
                print(order.client)
            order.save()
            return redirect(order.get_absolute_url())
        else:
            if client_form.is_valid():
                print('cos nie tak')
            messages.error(request, "coś poszło nie tak")
            return render(request, 'order_display/new_order.html', {'form': form, "client_form":client_form})
    form = OrderForm()
    client_form = ClientForm()
    return render(request, 'order_display/new_order.html', {'form': form, "client_form":client_form})


def show_searches(request):
    data = request.GET['search']
    print(data)
    searches = Client.objects.filter(
        Q(first_name__contains=data) | 
        Q(last_name__contains=data)
    )
    searches = list(searches.values())
    return JsonResponse({'searches':searches})


def finnish_element(request, element):
    element = Element.objects.get(slug = element)
    if element.status == Element.Status.DONE:
        element.status = Element.Status.IN_PROGRESS
    else: 
        element.status = Element.Status.DONE
    element.save()
    return redirect(element.order.get_absolute_url())

def finnish_order(request, order):
    order = Order.objects.get(slug = order)
    if order.status == Order.Status.PUBLISHED:
        order.status = Order.Status.FINISHED
    else: 
        order.status = Order.Status.PUBLISHED
    order.save()
    return redirect(order.get_absolute_url())


class Archive(LoginRequiredMixin, ListView):
    login_url = '/login/'
    queryset = Order.objects.filter(status = Order.Status.FINISHED)
    context_object_name = 'orders'
    template_name = 'order_display/order_list.html'

class Draft(LoginRequiredMixin, ListView):
    login_url = '/login/'
    queryset = Order.objects.filter(status = Order.Status.DRAFT)
    context_object_name = 'orders'
    template_name = 'order_display/order_list.html'
    
