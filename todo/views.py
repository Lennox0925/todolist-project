from django.shortcuts import render ,redirect
from django.http import HttpResponse
import json
from .models import Todo
from .forms import TodoForm
from datetime import datetime


def create_todo(request):
    message = ""
    form = TodoForm()
    # POST
    if request.method == "POST":
        form = TodoForm(request.POST)
        form.save()
        message = "建立成功"
        return redirect("todolist")
     
    return render(request, "todo/create-todo.html", {"message": message,"form": form})
   



def view_todo(request,id):
    message = ""
    try:
        todo = Todo.objects.get(id=id)
        form = TodoForm(instance=todo)
    except Exception as e:
        print(e)

    
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        todo = form.save(commit=False)

        if todo.completed:
            todo.date_completed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            todo.date_completed = None
        
        todo.save()
        message = "更新成功"
        return redirect("todolist")
        
    return render(request,"todo/view-todo.html", {"todo": todo,"form": form ,"message": message})






def todolist(request):
    # order_by("-created") 由新到舊排列
    todos = Todo.objects.all().order_by("-created")

    return render(request, "todo/todolist.html",{"todos": todos})

# Create your views here.
def index(request):
    return HttpResponse("<H1>Hello, world<H1>")


def books(request):
    my_books = {1:"Django", 2:"Python", 3:"JavaScript"}
    return HttpResponse(json.dumps(my_books),content_type = "application/json") 
