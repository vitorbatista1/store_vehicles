from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view, new_car_view, cars_sold_view
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("cars/", cars_view, name='cars_view'),
    path("new_car/", new_car_view, name='new_car_view'), 
    path("cars_sold/", cars_sold_view, name='cars_sold_view'), 
    path("register/", register_view, name='register_view'),
    path("login/", login_view, name='login_view'),
    path("logout/", logout_view, name='logout_view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
