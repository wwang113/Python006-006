from django.shortcuts import render
from .models import Dbdy

# Create your views here.
def douban_zs(request):
    shorts = Dbdy.objects.all()
    #start_value = Dbdy.objects.filter(starts__gt=3)
    items = Dbdy.objects.all()
    return render(request, 'index.html', locals())
