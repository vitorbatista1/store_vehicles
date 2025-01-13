from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms import carsModelForm
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


class CarsView(View):
    def get(self, request):
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



class NewCarView(CreateView):
    model = Car
    form_class = carsModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'



class CarDetailView(DetailView):
    model = Car
    template_name = 'car_details.html'


class UpdateCarView(UpdateView):
    model = Car
    form_class = carsModelForm
    template_name = 'update_car.html'
    
    def get_success_url(self):
        return reverse_lazy('car_details', kwargs={'pk': self.object.pk})

class DeleteCarView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/cars/'