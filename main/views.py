from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import Todo

# Create your views here.


def index(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'main/index.html', {'todo_items': todo_items})


@csrf_exempt
def addtodo(request):
    content = request.POST['content']
    now = timezone.now()
    added_date = now.strftime('%Y-%m-%d %H:%M:%S')
    r = Todo(added_date=added_date, text=content)
    r.save()
    return redirect('/')


@csrf_exempt
def delete_todo(request,item_id):
    Todo.objects.get(id=item_id).delete()
    return redirect('/')
