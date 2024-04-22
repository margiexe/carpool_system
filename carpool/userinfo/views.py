from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def info(request):
    context = {'page':'info'}
    return render(request,"info.html",context)

def about(request):
    context = {'page':'about'}
    return render(request,"about.html",context)

def receiver(request):
    context = {'page':'receiver'}
    return render(request,"receiver.html",context)

def allusers(request):
    if request.method == "POST" and ('name' in request.POST and 'roll_no' in request.POST and 'email' in request.POST and 'days' in request.POST and 'way' in request.POST and 'area' in request.POST):
        name = request.POST['name']
        roll_no = request.POST['roll_no']
        email = request.POST['email']
        days = request.POST['days']
        way = request.POST['way']
        area = request.POST['area']
            
        user_info.objects.create(name=name, roll_no=roll_no, email=email, days=days, way=way, area=area)
        return redirect('/info/allusers/')

    # Fetch data from both models
    receiver_data = user_info.objects.all()

    # Combine data into a single context dictionary
    context = {'receiver_data': receiver_data}

    # Render the template with the combined data
    return render(request, 'allusers.html', context)

# def allusers(request):
#     if request.method == "POST":
#         form = YourForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             roll_no = form.cleaned_data['roll_no']
#             email = form.cleaned_data['email']
#             days = form.cleaned_data['days']
#             way = form.cleaned_data['way']
#             area = form.cleaned_data['area']
            
#             try:
#                 user_info.objects.create(name=name, roll_no=roll_no, email=email, days=days, way=way, area=area)
#                 return redirect('/info/allusers/')
#             except Exception as e:
#                 print(e)  # Print the error for debugging purposes
#         else:
#             print(form.errors)  # Print form errors for debugging
    

#     receiver_data = user_info.objects.all()
#     context = {'receiver_data': receiver_data, 'form': form}
#     return render(request, 'allusers.html', context)