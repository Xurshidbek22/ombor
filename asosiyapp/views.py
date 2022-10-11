from django.shortcuts import render
from django.views import View
from .models import *


class BolimlarView(View):
    def get(self, request):
        return render(request, 'bulimlar.html')

class MahsulotlarView(View):
    def get(self, request):

        data = {
        'mahsulotlar':Mahsulot.objects.filter(sotuvchi__user=request.user)

        }
        return render(request, 'products.html', data)

class ClientView(View):
    def get(self, request):
        clt ={
            'clientlar':Sotuvchi.objects.filter(user=request.user)
        }

        return render(request, 'clients.html', clt)

class StatsView(View):
    def get(self, request):
        std ={
            'statuslar':Mahsulot.objects.filter(sotuvchi__user=request.user)
        }

        return render(request, 'stats.html', std)