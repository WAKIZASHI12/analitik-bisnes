from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ProcessForm, StepForm, TaskForm
from .models import Process, Step, Task



def view_processes(request):
    processes = Process.objects.all()
    return render(request, 'processes.html', {'processes': processes})

def create_process(request):
    if request.method == 'POST':
        form = ProcessForm(request.POST)
        if form.is_valid():
            process = form.save(commit=False)
            process.created_by = request.user
            process.save()
            return redirect(reverse('view_process', args=[process.id]))
    else:
        form = ProcessForm()
    return render(request, 'create_process.html', {'form': form})

def view_process(request, pk):
    process = get_object_or_404(Process, pk=pk)
    steps = process.steps.all().order_by('order')  # Обращение к связанным шагам через related_name
    tasks = []
    for step in steps:
        tasks += step.tasks.all()  # Обращение к связанным задачам через related_name
    context = {
        'process': process,
        'steps': steps,
        'tasks': tasks,
    }
    return render(request, 'view_process.html', context)