from django.urls import path

from .views import *

urlpatterns = [
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('clientlar/', ClientView.as_view(), name='clientlar'),
    path('client_update/<int:son>/', ClientUpdateView.as_view(), name='client_update'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('pr_delete/<int:pk>/', ProductDelete.as_view(), name='pr_delete'),
    path('cl_delete/<int:son>/', ClientDelete.as_view(), name='cl_delete')

]
