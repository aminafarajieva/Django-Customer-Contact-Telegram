from django.shortcuts import render
from CustomerContactBot.sendmessage import sendMessage
from .models import Order
from .forms import OrderForm


# Create your views here.

def main(request):
    form = OrderForm()
    return render(request,'./index.html',{'form':form})


def contact(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name = name, order_phone = phone)
    element.save()
    sendMessage()
    return render(request,'./thanks.html',{'name':name})