from django.shortcuts import render, redirect

from .models import Queue

def enqueue(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	context = {}
	if request.method == "POST":
		users = Queue.objects.all()
		for user in users:
			if user.user == request.user:
				return redirect('/')
		Queue.objects.create(user = request.user)
	return redirect('/')