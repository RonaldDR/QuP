from django.shortcuts import render, redirect

from .models import Window1Queue, Window2Queue, Window3Queue, Window4Queue, Window5Queue
from django.contrib.auth.models import User
from registration.models import UserStatus

def window1enqueue(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	context = {}
	if request.method == "POST":
		userr = User.objects.get(username = request.user.username)
		userr_status = UserStatus.objects.get(user = userr)
		if userr_status.status == "true":
			return redirect('/')
		users = Window1Queue.objects.all()
		for user in users:
			if user.user == request.user:
				return redirect('/')
		Window1Queue.objects.create(user = request.user)
		userr_statuss = UserStatus.objects.filter(user = userr)
		userr_statuss.update(status="true")
	return redirect('/')

def window1dequeue(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	context = {}
	if request.method == "POST":
		userr = User.objects.get(username = request.user.username)
		userr_status = UserStatus.objects.get(user = userr)
		if userr_status.status == "false":
			return redirect('/')
		if userr_status.status == "true":
			user = Window1Queue.objects.filter(user = userr)
			user.delete()
		userr_statuss = UserStatus.objects.filter(user = userr)
		userr_statuss.update(status="false")
	return redirect('/')

def window2enqueue(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	context = {}
	if request.method == "POST":
		userr = User.objects.get(username = request.user.username)
		userr_status = UserStatus.objects.get(user = userr)
		if userr_status.status == "true":
			return redirect('/')
		users = Window2Queue.objects.all()
		for user in users:
			if user.user == request.user:
				return redirect('/')
		Window2Queue.objects.create(user = request.user)
		userr_statuss = UserStatus.objects.filter(user = userr)
		userr_statuss.update(status="true")
	return redirect('/')

def window2dequeue(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	context = {}
	if request.method == "POST":
		userr = User.objects.get(username = request.user.username)
		userr_status = UserStatus.objects.get(user = userr)
		if userr_status.status == "false":
			return redirect('/')
		if userr_status.status == "true":
			user = Window2Queue.objects.filter(user = userr)
			user.delete()
		userr_statuss = UserStatus.objects.filter(user = userr)
		userr_statuss.update(status="false")
	return redirect('/')

def window3enqueue(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	context = {}
	if request.method == "POST":
		userr = User.objects.get(username = request.user.username)
		userr_status = UserStatus.objects.get(user = userr)
		if userr_status.status == "true":
			return redirect('/')
		users = Window3Queue.objects.all()
		for user in users:
			if user.user == request.user:
				return redirect('/')
		Window3Queue.objects.create(user = request.user)
		userr_statuss = UserStatus.objects.filter(user = userr)
		userr_statuss.update(status="true")
	return redirect('/')

def window3dequeue(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	context = {}
	if request.method == "POST":
		userr = User.objects.get(username = request.user.username)
		userr_status = UserStatus.objects.get(user = userr)
		if userr_status.status == "false":
			return redirect('/')
		if userr_status.status == "true":
			user = Window3Queue.objects.filter(user = userr)
			user.delete()
		userr_statuss = UserStatus.objects.filter(user = userr)
		userr_statuss.update(status="false")
	return redirect('/')

def window4enqueue(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	context = {}
	if request.method == "POST":
		userr = User.objects.get(username = request.user.username)
		userr_status = UserStatus.objects.get(user = userr)
		if userr_status.status == "true":
			return redirect('/')
		users = Window4Queue.objects.all()
		for user in users:
			if user.user == request.user:
				return redirect('/')
		Window4Queue.objects.create(user = request.user)
		userr_statuss = UserStatus.objects.filter(user = userr)
		userr_statuss.update(status="true")
	return redirect('/')

def window4dequeue(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	context = {}
	if request.method == "POST":
		userr = User.objects.get(username = request.user.username)
		userr_status = UserStatus.objects.get(user = userr)
		if userr_status.status == "false":
			return redirect('/')
		if userr_status.status == "true":
			user = Window4Queue.objects.filter(user = userr)
			user.delete()
		userr_statuss = UserStatus.objects.filter(user = userr)
		userr_statuss.update(status="false")
	return redirect('/')

def window5enqueue(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	if request.method == "POST":
		userr = User.objects.get(username = request.user.username)
		userr_status = UserStatus.objects.get(user = userr)
		if userr_status.status == "true":
			return redirect('/')
		users = Window5Queue.objects.all()
		for user in users:
			if user.user == request.user:
				return redirect('/')
		Window5Queue.objects.create(user = request.user)
		userr_statuss = UserStatus.objects.filter(user = userr)
		userr_statuss.update(status="true")
	return redirect('/')

def window5dequeue(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	context = {}
	if request.method == "POST":
		userr = User.objects.get(username = request.user.username)
		userr_status = UserStatus.objects.get(user = userr)
		if userr_status.status == "false":
			return redirect('/')
		if userr_status.status == "true":
			user = Window5Queue.objects.filter(user = userr)
			user.delete()
		userr_statuss = UserStatus.objects.filter(user = userr)
		userr_statuss.update(status="false")
	return redirect('/')