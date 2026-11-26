from django.shortcuts import render ,redirect 
from .form import PersonForm
from django.http import HttpResponse,HttpResponseBadRequest
from .infoForm import InfoForm
from todos import form
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
       form = PersonForm(request.POST)
       if form.is_valid():
        name = form.cleaned_data['name']
        age = form.cleaned_data['age']
        job = form.cleaned_data['job']
        return render(request, "todos/render.html", {"name": name, "age": age, "job": job})
    else :
        return render(request, "todos/error.html")

def submit_examples(request):
    form = PersonForm()
    return render(request, "todos/form.html", {"form": form})


def template_view(request):
    context = {
        "name": "John Doe",
        "age": 30,
        "skills": ['Engineer', 'Developer', 'Designer'],   

    }
    return render(request , 'todos/template.html', context)



def get_info(request):
    if request.method == "POST":
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            return render(request , "image/image.html", {'image': image})

        else :
            return HttpResponseBadRequest("Invalid form submission.")