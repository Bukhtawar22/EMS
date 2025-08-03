from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Orderpy
# Create your views here.

def home(request):
    ords= Orderpy.objects.all()
    return render(request,"index.html",{'ords':ords})

def order_add(request):
     if request.method =="POST":
        #data fetch
      
        person_name = request.POST.get("per_name")
        order_food = request.POST.get("or_food")
        order_drink = request.POST.get("or_drink")
        
         # Prices dictionary
        food_prices = {
            "Beef Burgar": 250,
            "Chicken Burgar": 200,
            "Chips": 100,
            "Chicken Roll": 150,
            "Pizza --Small": 400,
            "Pizza --Medium": 600,
            "Pizza --Large": 900,
        }
        drink_prices = {
            "Pepsi": 50,
            "Cola": 50,
            "Pakola": 40,
            "7up": 50,
            "Normal Water": 30,
        }
        food_price=food_price.get(order_food,0)
        drink_price=drink_price.get(order_drink,0)
        total_price=food_price+drink_price

        #validate
        #create models objects and set the data

        o=Orderpy()
        o.per_name=person_name
        o.orderfood=order_food
        o.orderdrink=order_drink
        o.food_price = food_price
        o.drink_price = drink_price
        o.total_price = total_price
      #save the object
        o.save()

      #prepare msg
        print("yes")
        return redirect("/py_res/home/")
     return render(request,"orderadd.html")

def bill(request):
    ords= Orderpy.objects.all()
    return render(request,"bill.html",{'ords':ords})

