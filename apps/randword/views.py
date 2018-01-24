from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
	

def index(request):
	return render(request, 'randomword/index.html')

def generate(request):
	if 'clicks' not in request.session:
		request.session['clicks']=0

	request.session['clicks']+=1
	word=get_random_string(length=12)
	context={
		'word': word
	}
	return render(request, 'randomword/index.html', context)

def reset(request):
	request.session['clicks']=0
	return redirect('/')