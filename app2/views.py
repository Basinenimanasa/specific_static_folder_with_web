from django.shortcuts import render

# Create your views here.
def registrationformpage(request):
    return render(request,'registrationformpage.html')
def formpage(request):
    return render(request,'formpage.html')