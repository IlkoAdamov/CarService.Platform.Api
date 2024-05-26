from django.urls import path, include
from carservice_api import views
from django.conf import settings

urlpatterns = [
    path('cars/', views.get_list_of_cars),
    path('cars/create', views.create_car_item),
    path('cars/update/<int:id>/', views.update_car_item),
    # path('cars/delete', views.delete_car_item),

    path('maintenance/', views.get_list_of_maintenances),
    path('maintenance/carId/<int:car_id>/', views.get_list_of_maintenances_byCarId),
    path('maintenance/create', views.create_maintenance_item),
    # path('maintenance/update', views.update_maintenance_item),
    # path('maintenance/delete', views.delete_maintenance_item),

    path('service/maintenanceId/<int:maintenance_id>/', views.get_list_of_service_byMaintenanceId),
    path('service/create', views.create_service_item)
]