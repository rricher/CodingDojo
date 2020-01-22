from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if request.method == 'GET':
        # quantity_from_form = int(request.POST["quantity"])
        # price_from_form = float(request.POST["price"])
        # total_charge = quantity_from_form * price_from_form
        # print("Charging credit card...")
        # Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        # return render(request, "store/checkout.html")
        orders = Order.objects.all()
        total_items = 0
        total_price = 0
        for order in orders:
            total_items += order.quantity_ordered
            total_price += order.total_price
        context = {
            "last_order": Order.objects.last(),
            "items": total_items,
            "price": total_price,
        }
        return render(request, "store/checkout.html", context)
    if request.method == 'POST':
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = Product.objects.get(id=int(request.POST["price"])).price
        total_charge = quantity_from_form * price_from_form
        print(f"Charging credit card {price_from_form}")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        return redirect("/checkout")