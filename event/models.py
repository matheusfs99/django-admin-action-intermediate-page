from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    date = models.DateTimeField(verbose_name="Data e Hora")
    locale = models.CharField(max_length=255, verbose_name="Local")
    is_active = models.BooleanField(default=False, verbose_name="Evento Ativo")

    def __str__(self):
        return self.title


class Participant(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="participants", verbose_name="Evento")
    registered_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Data do Registro")

    class Meta:
        unique_together = ("email", "event")
    
    def __str__(self):
        return f"{self.name} - {self.email}"
