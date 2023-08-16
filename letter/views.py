from django.shortcuts import render, redirect
from .models import Letter

# Create your views here.
def letter_log(request):
    letters = Letter.objects.filter()
    return render(request, 'letter/letter_log.html', {'letters':letters})