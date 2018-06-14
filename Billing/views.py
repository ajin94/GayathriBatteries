from django.shortcuts import render

# Create your views here.


def billing_landing(request):
    return render(request, 'Billing/index.html')
