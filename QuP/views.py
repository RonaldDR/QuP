
from django.shortcuts import render
from django.contrib.auth.models import User

from queues.models import Queue

def home(request):
	context = {
		'queues': Queue.objects.all(),
	}

	return render(request, 'home.html', context=context);

