from django.shortcuts import render, redirect

from .models import Window1Queue, Window2Queue, Window3Queue, Window4Queue, Window5Queue
from django.contrib.auth.models import User
from registration.models import UserStatus

# --------------------------window1-------------------------------
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
		userr_status = UserStatus.objects.filter(user = userr)
		if Window1Queue.objects.filter(user = userr).count() > 0:
			Window1Queue.objects.filter(user = userr).delete()
			userr_status.update(status="false")
	return redirect('/')

def window1pop(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	if request.method == "POST":
		if Window1Queue.objects.all().count() > 0:
			users = Window1Queue.objects.all().first()
			userr_status = UserStatus.objects.filter(user = users.user)
			userr_status.update(status="false")
			users.delete()
	return redirect('/')

# ---------------------------------window2-----------------------------------------
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
		userr_status = UserStatus.objects.filter(user = userr)
		if Window2Queue.objects.filter(user = userr).count() > 0:
			Window2Queue.objects.filter(user = userr).delete()
			userr_status.update(status="false")
	return redirect('/')

def window2pop(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	if request.method == "POST":
		if Window2Queue.objects.all().count() > 0:
			users = Window2Queue.objects.all().first()
			userr_status = UserStatus.objects.filter(user = users.user)
			userr_status.update(status="false")
			users.delete()

	return redirect('/')
# --------------------------------window3---------------------------------
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
		userr_status = UserStatus.objects.filter(user = userr)
		if Window3Queue.objects.filter(user = userr).count() > 0:
			Window3Queue.objects.filter(user = userr).delete()
			userr_status.update(status="false")
	return redirect('/')

def window3pop(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	if request.method == "POST":
		if Window3Queue.objects.all().count() > 0:
			users = Window3Queue.objects.all().first()
			userr_status = UserStatus.objects.filter(user = users.user)
			userr_status.update(status="false")
			users.delete()
	return redirect('/')
# -------------------------------window4------------------------------
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
		userr_status = UserStatus.objects.filter(user = userr)
		if Window4Queue.objects.filter(user = userr).count() > 0:
			Window4Queue.objects.filter(user = userr).delete()
			userr_status.update(status="false")
	return redirect('/')

def window4pop(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	if request.method == "POST":
		if Window4Queue.objects.all().count() > 0:
			users = Window4Queue.objects.all().first()
			userr_status = UserStatus.objects.filter(user = users.user)
			userr_status.update(status="false")
			users.delete()
	return redirect('/')
# -------------------------------window5-------------------------------
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
		userr_status = UserStatus.objects.filter(user = userr)
		if Window5Queue.objects.filter(user = userr).count() > 0:
			Window5Queue.objects.filter(user = userr).delete()
			userr_status.update(status="false")
	return redirect('/')

def window5pop(request):
	if not request.user.is_authenticated:
		return redirect(reverse('sign_in'))
	if request.method == "POST":
		if Window5Queue.objects.all().count() > 0:
			users = Window5Queue.objects.all().first()
			userr_status = UserStatus.objects.filter(user = users.user)
			userr_status.update(status="false")
			users.delete()
	return redirect('/')