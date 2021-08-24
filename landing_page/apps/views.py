from django.shortcuts import render
from .models import App


def apps_index(request):
	apps = App.objects.all()
	data = {'apps': apps}
	return render(request, 'apps/apps_index.html', data)

def app(request, name):
	try:
		app = App.objects.get(title=name)
		data = {'app': app}
	except:
		data = {'message': 'L\'app que vous avez demandé n\'existe pas'}
	return render(request, 'apps/app.html', data) 