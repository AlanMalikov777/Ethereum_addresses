from turtle import back
from django.shortcuts import render, redirect
from . models import Ether
from . forms import ProductForm
from .  jigan import ethpullacc, ethpullbal

# Create your views here.

def index(request):
    account = []
    balance = []
    if request.method == "POST":
        account = ethpullacc()
        balance = ethpullbal()
    context = {
            "account": account,
            "balance": balance,
        }

    return render(request, 'chartapp/index.html', context)
