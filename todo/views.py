from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Todo



def create_todo(request):
    message = ""

    # POST
    if request.method == "POST":
        print(request.POST)
        title = request.POST.get("title")
        if title== "":
            print("標題欄位不能為空")
            message = "標題欄位不能為空"
        else:
            text = request.POST.get("text")
            important = request.POST.get("important")

            important = True if important == "on" else False
        
            # 建立資料
            todo = Todo.objects.create(title=title,text=text,important=important)
            todo.save()
            message = "建立成功"
     
    return render(request, "todo/create-todo.html", {"message": message})
   


# 1.新增view-todo.html
# 2.將todo傳出到{{todo}}
def view_todo(request,id):
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)
        
    return render(request,"todo/view-todo.html", {"todo": todo})


def todolist(request):
    todos = Todo.objects.all()

    return render(request, "todo/todolist.html",{"todos": todos})

# Create your views here.
def index(request):
    return HttpResponse("<H1>Hello, world<H1>")


def books(request):
    my_books = {1:"Django", 2:"Python", 3:"JavaScript"}
    return HttpResponse(json.dumps(my_books),content_type = "application/json") 
