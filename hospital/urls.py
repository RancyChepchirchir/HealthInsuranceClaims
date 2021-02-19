from django.urls import path
from . import views

urlpatterns = [
    # ! params ; path name, view name, url name
    path('hospitalsdata/', views.getHospitals, name='allhospitals')

]
