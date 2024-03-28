from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect

class MuallifView(View):
    def get(self,request):
        return render(request,'Muallif.html')


class MaqolaView(View):
    def get(self,request):
        return render(request,'Maqola.html')
