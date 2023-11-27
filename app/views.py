from django.shortcuts import render

# Create your views here.
def joke(request):
    return render(request,'joker.html')