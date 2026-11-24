from django.shortcuts import render ,redirect 

from django.http import HttpResponse,HttpResponseBadRequest
def hello_world(request):
    return HttpResponse("Hello, World!")
# Create your views here.


def hello_world_py(request):
    return HttpResponse("Hello, World! from Python")


def hello_world_html(request):
    return render(request, "todos/hello.html")

def hello_world_html_name(request, name):
    return HttpResponse(f"Hello, {name}! from HTML")

def hello_world_query(request):
    return HttpResponse(f'your Search Query is {request.GET.get('q')}')

def hello_world_redirect(request):
    return redirect('hello_world_html')


def post_examples(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        job = request.POST.get('job')
        return render(request, "todos/render.html", {"name": name, "age": age, "job": job})
    else :
        return render(request, "todos/error.html")

def submit_examples(request):
    return render(request, "todos/form.html")