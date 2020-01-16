from django.shortcuts import render, redirect
from main.models import link_uch, link_interesting, liberi, link_oge_ege, link_olimpiads, about_me, Post_a, Post_g


def glavnaya(request):
    menu_uch = link_uch.objects.order_by()
    return render(request,'main/glavnaya.html', {'menu_uch':menu_uch})

def aboutme(request):
    menu_uch = link_uch.objects.order_by()
    about = about_me.objects.all()
    return render(request,'main/about_me.html', {'menu_uch':menu_uch, 'about':about})

def algebra(request):
    a = Post_a.objects.order_by()
    menu_uch = link_uch.objects.order_by()
    return render(request,'main/algebra.html', {'menu_uch':menu_uch, 'a':a})

def geometria(request):
    g = Post_g.objects.order_by()
    menu_uch = link_uch.objects.order_by()
    return render(request,'main/geometria.html', {'menu_uch':menu_uch, 'g':g})


def oge_ege(request):
    menu_uch = link_uch.objects.order_by()
    links = link_oge_ege.objects.all()
    return render(request,'main/oge_ege.html', {'menu_uch':menu_uch, 'links':links})

def interesting(request):
    menu_uch = link_uch.objects.order_by()
    links = link_interesting.objects.all()
    return render(request,'main/interesting.html', {'menu_uch':menu_uch, 'links':links})

def library(request):
    menu_uch = link_uch.objects.order_by()
    links = liberi.objects.all()
    return render(request,'main/library.html', {'menu_uch':menu_uch, 'links':links})

def olimpiads(request):
    menu_uch = link_uch.objects.order_by()
    links = link_olimpiads.objects.all()
    return render(request,'main/olimpiads.html', {'menu_uch':menu_uch, 'links':links})




