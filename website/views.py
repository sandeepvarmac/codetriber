from django.shortcuts import render

# Create your views here.
def homepage(request):
	#return HttpResponse('This is an <strong>awesome</strong> tutorial webasite')
	return render(
		request = request,
		template_name = 'index.html',
		context = {}
		)
