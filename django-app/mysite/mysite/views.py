from django.http import HttpResponse
from django.shortcuts import render
def aboutus(resquest):
	return HttpResponse("this is about us page")

def courseDetails(resquest, courseid):
	return HttpResponse(courseid)

def homePage(request):
	data={
		'title':'Home Page',
		'description' : 'This is First Django Test Page '
	}
	return render(request,"index.html", data)	