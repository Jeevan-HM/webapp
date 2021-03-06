from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("electronics", views.electronics, name="electronics"),
    path("fashion", views.fashion, name="fashion"),
    path("home", views.home, name="home"),
    path("others", views.others, name="others"),
    path("allproducts", views.allproducts, name="allproducts"),
    path("mobile", views.mobile, name="mobile"),
    path("computer", views.computer, name="computer"),
    path("malegarment", views.malegarment, name="malegarment"),
    path("femalegarment", views.femalegarment, name="femalegarment"),
    path("boysgarment", views.boysgarment, name="boysgarment"),
    path("girlsgarment", views.girlsgarment, name="girlsgarment"),
    path("dummystand", views.dummystand, name="dummystand"),
    path("femalefootwear", views.femalefootwear, name="femalefootwear"),
    path("boysfootwear", views.boysfootwear, name="boysfootwear"),
    path("girlsfootwear", views.girlsfootwear, name="girlsfootwear"),
    path("kidsfootwear", views.kidsfootwear, name="kidsfootwear"),
    path("malefootwear", views.malefootwear, name="malefootwear"),
    path("perfume", views.perfume, name="perfume"),
    path("cosmetics", views.cosmetics, name="cosmetics"),
    path("jwellery", views.jwellery, name="jwellery"),
    path("watches", views.watches, name="watches"),
    path("belt", views.belt, name="belt"),
    path("wallet", views.wallet, name="wallet"),
    path("google", views.google, name="google"),
    path("seagenable", views.seagenable, name="seagenable"),
    path("sport", views.sport, name="sport"),
    path("play", views.play, name="play"),
    path("gifts", views.gifts, name="gifts"),
    path("crockery", views.crockery, name="crockery"),
    path("kitchenware", views.kitchenware, name="kitchenware"),
    path("handloom", views.handloom, name="handloom"),
    path("plastic", views.plastic, name="plastic"),
    path("cleaning", views.cleaning, name="cleaning"),
    path("tools", views.tools, name="tools"),
    path("index", views.index, name="index"),
    path("others", views.other, name="others"),
    path("gifts", views.gifts, name="gifts"),
    # path("about", views.about, name="about"),
]
