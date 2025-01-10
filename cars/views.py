from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms import carsModelForm

def cars_view(request):
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(model__icontains=search, sold=False)
    else:
        cars = Car.objects.filter(sold=False).order_by('model', 'brand')
    return render(
        request,
        'cars.html', 
        {'cars': cars }
    )
def cars_sold_view(request):
    cars = Car.objects.filter(sold=True).order_by('model').order_by('brand')
    return render(
        request,
        'sold_cars.html', 
        {'cars': cars }
    )

def new_car_view(request):
    if request.method == 'POST':
        new_car_form = carsModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_view')
    else:
        new_car_form = carsModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})