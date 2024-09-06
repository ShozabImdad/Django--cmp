from django.shortcuts import render
from .models import JewelVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def first_app(request):
    jewels = JewelVariety.objects.all()
    return render(request, 'first/first_app.html', {'jewels': jewels})


def jewel_detail(request, jewel_id):
    jewel = get_object_or_404(JewelVariety, pk= jewel_id)
    return render(request, 'first/detail.html', {{'jewel', jewel}})
    