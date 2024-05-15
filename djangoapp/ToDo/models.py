from django.db import models

class ToDo(models.Model):
  name = models.CharField("Nome da Tarefa", max_length=100)
  description = models.TextField("Descrição da tarefa")
  status = models.BooleanField("Status da tarefa")
  created_at = models.DateTimeField("Data de Criação", auto_now=True)
  updated_at = models.DateField("Data de atualização", auto_now=True)
  
  def __str__(self) -> str:
    return self.name