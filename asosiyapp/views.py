from django.shortcuts import render,redirect
from django.views import View
from .models import *

class ProductDelete(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            hozirgi_sotuvchi = Sotuvchi.objects.filter(user=request.user)[0]
            m = Mahsulot.objects.get(id=pk)
            if m.sotuvchi == hozirgi_sotuvchi and request.user.is_staff:
                m.delete()
                return redirect('/bolimlar/mahsulotlar/')
        return redirect('login')

class ClientDelete(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            mijoz = Sotuvchi.objects.filter(user=request.user)[0]
            m = Mijoz.objects.get(id=son)
            if m.sotuvchi == mijoz and request.user.is_staff:
                m.delete()
            return redirect('/bolimlar/clientlar/')
        return redirect('login')

class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        else:
            redirect('/')

class MahsulotlarView(View):

    def post(self, request):
        Mahsulot.objects.create(
            nom=request.POST.get('pr_name'),
            narx=request.POST.get('pr_price'),
            miqdor=request.POST.get('pr_amount'),
            brend=request.POST.get('pr_brand'),
            olchov=request.POST.get('olchov'),
            sotuvchi=Sotuvchi.objects.filter(user=request.user)[0]
        )
        redirect('/bolimlar/mahsulotlar/')

        return render(request, 'products.html')

    def get(self, request):
        data = {
        'mahsulotlar':Mahsulot.objects.filter(sotuvchi__user=request.user)

        }
        return render(request, 'products.html', data)



class ClientView(View):
    def post(self, request):
        Mijoz.objects.create(
            ism=request.POST.get('client_name'),
            nom=request.POST.get('client_shop'),
            manzil=request.POST.get('client_address'),
            tel=request.POST.get('client_phone'),
            qarz=request.POST.get('qarzi'),
            sotuvchi=Sotuvchi.objects.filter(user=request.user)[0]
        )
        redirect('/bolimlar/clientlar/')

        return render(request, 'clients.html')

    def get(self, request):

        clt ={
            'clientlar':Mijoz.objects.filter(sotuvchi__user=request.user)
        }

        return render(request, 'clients.html', clt)


class ClientUpdateView(View):
    def get(self, request, son):
        std ={
            'client':Mijoz.objects.get(id=son)

        }
        return render(request, 'client_update.html', std)

    def post(self, request, son):
        if request.user.is_authenticated:
            mijoz = Sotuvchi.objects.filter(user=request.user)[0]
            if request.user.is_staff and Mijoz.objects.get(id=son).sotuvchi == mijoz:
                Mijoz.objects.filter(id=son).update(
                    ism=request.POST.get('client_name'),
                    nom=request.POST.get('client_shop'),
                    tel=request.POST.get('client_phone'),
                    manzil=request.POST.get('client_address'),
                    qarz=request.POST.get('client_qarzi'),
                    sotuvchi=mijoz
                )
                return redirect('/bolimlar/clientlar/')



class StatsView(View):
    def get(self, request):
        std ={
            'statuslar':Mahsulot.objects.filter(sotuvchi__user=request.user)
        }

        return render(request, 'stats.html', std)