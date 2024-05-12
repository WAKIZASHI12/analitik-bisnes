from django.db import models

from django.contrib.auth.models import User

class Process(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def str(self):
        return self.name

class Step(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='steps')  # Обратная связь с Process
    order = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    

    def str(self):
        return self.title
    
    
# Создание модели задач:

class Task(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_data = models.DateField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
         return self.title