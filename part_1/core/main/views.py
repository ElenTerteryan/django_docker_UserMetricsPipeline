from django.shortcuts import render
from .models import MeetingInfo
# Create your views here.


def index(request):
    meet = MeetingInfo.objects.all()
    return render(request, 'index.html', context={
        'meet':meet
    })