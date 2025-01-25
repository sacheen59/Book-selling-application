from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based
# class based views

def index(request):
    return HttpResponse('This is my firstpage.')

def homepage(request):
    list_student = [
        {
            "name":"sachin",
            "course":"python",
        },
        {
            "name": "Zenith",
            "course": "React"
        },
        {
            "name": "Tripti",
            "course": "Graphics"
        },
        {
            "name": "Bandana",
            "course": "Python"
        }
    ]


    context = {
        'data': list_student
    }
    return render(request,"books/index.html",context)


# books = [
#     {
#         "name": 
#         "price"
#         "instock"
#         "description"
#         "author"
#         "published date"
#     }


# ]