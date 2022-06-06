from django.shortcuts import render
from .models import Consulting


# Create your views here.
def consulting(request):
    all_consulting = Consulting.objects.all().order_by('consulting_id')
    return render(request, 'consulting/consulting.html', {'consulting': all_consulting})
