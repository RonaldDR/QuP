
from django.shortcuts import render
from django.contrib.auth.models import User

from queues.models import Window1Queue, Window2Queue, Window3Queue, Window4Queue, Window5Queue

def home(request):
	context = {
		'window1queues': Window1Queue.objects.all(),
		'window2queues': Window2Queue.objects.all(),
		'window3queues': Window3Queue.objects.all(),
		'window4queues': Window4Queue.objects.all(),
		'window5queues': Window5Queue.objects.all(),

		'window1top': Window1Queue.objects.all().first(),
		'window2top': Window2Queue.objects.all().first(),
		'window3top': Window3Queue.objects.all().first(),
		'window4top': Window4Queue.objects.all().first(),
		'window5top': Window5Queue.objects.all().first(),
	}

	return render(request, 'home.html', context=context);
