from django.shortcuts import render, redirect
from .models import Products
from django.core.paginator import Paginator


# products = Products.objects.all()


def index(request):
    products = Products.objects.order_by("?")
    return render(request, "index.html")


def electronics(request):
    products = Products.objects.order_by("?")
    return render(request, "electronics.html", {"products": products})


def other(request):
    products = Products.objects.order_by("?")
    return render(request, "others.html", {"products": products})


def home(request):
    products = Products.objects.order_by("?")
    return render(request, "home.html", {"products": products})


def others(request):
    products = Products.objects.order_by("?")
    return render(request, "others.html", {"products": products})


def fashion(request):
    products = Products.objects.order_by("?")
    return render(request, "fashion.html", {"products": products})


def allproducts(request):
    products = Products.objects.order_by("?")
    return render(request, "allproducts.html", {"products": products})


def mobile(request):
    products = Products.objects.order_by("?")
    return render(request, "mobile.html", {"products": products})


def computer(request):
    products = Products.objects.order_by("?")
    return render(request, "computer.html", {"products": products})


def contact(request):
    products = Products.objects.order_by("?")
    return render(request, "contact.html", {"products": products})


def dummystand(request):
    products = Products.objects.order_by("?")
    return render(request, "dummystand.html", {"products": products})


def girlsgarment(request):
    products = Products.objects.order_by("?")
    return render(request, "girlsgarment.html", {"products": products})


def femalegarment(request):
    products = Products.objects.order_by("?")   
    return render(
        request, "femalegarment.html", {"products": products}
    )


def boysgarment(request):
    products = Products.objects.order_by("?")
    return render(request, "boysgarment.html", {"products": products})


def malegarment(request):
    products = Products.objects.order_by("?")
    return render(request, "malegarment.html", {"products": products})


def femalefootwear(request):
    products = Products.objects.order_by("?")
    return render(
        request, "femalefootwear.html", {"products": products}
    )


def boysfootwear(request):
    products = Products.objects.order_by("?")
    return render(request, "boysfootwear.html", {"products": products})


def girlsfootwear(request):
    products = Products.objects.order_by("?")
    return render(
        request, "girlsfootwear.html", {"products": products}
    )


def kidsfootwear(request):
    products = Products.objects.order_by("?")
    return render(request, "kidsfootwear.html", {"products": products})


def malefootwear(request):
    products = Products.objects.order_by("?")
    return render(request, "malefootwear.html", {"products": products})


def perfume(request):
    products = Products.objects.order_by("?")
    return render(request, "perfume.html", {"products": products})


def cosmetics(request):
    products = Products.objects.order_by("?")  
    return render(
        request, "cosmetics.html", {"products": products}
    )


def google(request):
    products = Products.objects.order_by("?")
    return render(request, "google.html", {"products": products})


def wallet(request):
    products = Products.objects.order_by("?")
    return render(request, "wallet.html", {"products": products})


def jwellery(request):
    products = Products.objects.order_by("?")
    return render(request, "jwellery.html", {"products": products})


def watches(request):
    products = Products.objects.order_by("?")
    return render(request, "watches.html", {"products": products})


def belt(request):
    products = Products.objects.order_by("?")
    return render(request, "belt.html", {"products": products})


def seagenable(request):
    products = Products.objects.order_by("?")
    return render(request, "seagenable.html", {"products": products})


def gifts(request):
    products = Products.objects.order_by("?")
    return render(request, "gifts.html", {"products": products})


def play(request):
    products = Products.objects.order_by("?")
    return render(request, "play.html", {"products": products})


def sport(request):
    products = Products.objects.order_by("?")
    return render(request, "sport.html", {"products": products})


def crockery(request):
    products = Products.objects.order_by("?")
    return render(request, "crockery.html", {"products": products})


def handloom(request):

    products = Products.objects.order_by("?")
    return render(request, "handloom.html", {"products": products})


def plastic(request):   
    products = Products.objects.order_by("?")
    return render(request, "plastic.html", {"products": products})


def cleaning(request):
    products = Products.objects.order_by("?")
    return render(request, "cleaning.html", {"products": products})


def tools(request):
    products = Products.objects.order_by("?")
    return render(request, "tools.html", {"products": products})


def kitchenware(request):
    products = Products.objects.order_by("?")
    return render(request, "kitchenware.html", {"products": products})
