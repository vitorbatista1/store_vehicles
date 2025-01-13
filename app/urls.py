from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_sold_view, CarsView, NewCarView, CarDetailView, UpdateCarView
from accounts.views import register_view, login_view, logout_view



urlpatterns = [
    path("admin/", admin.site.urls),
    path("cars/", CarsView.as_view(), name='cars_view'),
    path("new_car/", NewCarView.as_view(), name='new_car_view'), 
    path("cars_sold/", cars_sold_view, name='cars_sold_view'), 
    path("register/", register_view, name='register_view'),
    path("login/", login_view, name='login_view'),
    path("logout/", logout_view, name='logout_view'),
    path("car/<int:pk>/", CarDetailView.as_view(), name='car_details'),
    path("car/<int:pk>/update/", UpdateCarView.as_view(), name='car_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
