from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from webapp.forms import TaskForm
from webapp.models import Tasks


def index_view(request, *args, **kwargs):
    to_do_ls = Tasks.objects.all()
    return render(request, 'index.html', context={
        'tasks': to_do_ls
    })

def task_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })

def task_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        print('create')
        print(form)
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Tasks.objects.create(
                title=form.cleaned_data['title'],
                status=form.cleaned_data['status'],
                description=form.cleaned_data['description'],
                created_at=form.cleaned_data['created_at']
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})

def task_edit_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'update.html', context={'task': task,'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = request.POST.get('title')
            task.status = request.POST.get('status')
            task.description = request.POST.get('description')
            task.created_at = request.POST.get('created_at')
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update.html', context={'task': task, 'form': form})
    return redirect('task_view', pk=task.pk)

def task_delete_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')