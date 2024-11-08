from django.shortcuts import render
from django.views import View
from .models import Item
# Create your views here.
class Home(View):
    def get(self, request):
        items = Item.objects.all()
        context = {
            'items':items,
        }
        return render(request, 'base/index.html', context=context)