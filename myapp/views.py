from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import TODO
# Create your views here.

# here i preview the home page with all todo list (todo, done)
def index(request):
    list_todo=TODO.objects.all()
    if request.method=='POST':
        todo(request)
        return redirect('/',{'todos':list_todo})
    else:
        return render(request,'index.html',{'todos':list_todo})
# responsible for save the todo in database
#in the home page will appear done buttone
def todo(request):
    newTodo =TODO(
        details = request.POST['details'],
        status = 'todo'
    )
    newTodo.save()

# responsible for change status of the todo so that it appear with line-through
#and the button will change from done to delete in the home page

def done(request,id):
    del_todo=TODO.objects.get(id=id)
    del_todo.status='done'
    del_todo.save()
    return redirect('/')
    
# responsible for delete the todo from db and change status to delete
#and the to do will not appear 

def delete(request,id):
    del_todo=TODO.objects.get(id=id)
    del_todo.status='delete'
    del_todo.delete()
    del_todo.save()
    return redirect('/')