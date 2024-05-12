from django import forms
from .models import Process, Step, Task

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['name', 'description']

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['title', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
