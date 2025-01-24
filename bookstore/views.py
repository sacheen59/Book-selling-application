from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1> This is homepage </h1>")

def aboutpage(request):
    return HttpResponse("<h1>This is about page</h1>")