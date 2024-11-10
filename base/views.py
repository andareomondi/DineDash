from django.shortcuts import render
from django.views import View
from .models import Product
from django.http import JsonResponse
# Create your views here.
class Home(View):
    def get(self, request):
        items = Product.objects.all()
        context = {
            'items':items,
        }
        return render(request, 'base/index.html', context=context)
    def post(self, request):
        value = request.POST.get('value')
        print(value)
        return render(request, 'base/index.html')
    
class Test(View):
    def get(self, request):
        data = {
            'name': 'John',
        }
        return JsonResponse(data)

