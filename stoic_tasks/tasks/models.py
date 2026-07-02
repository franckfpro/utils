from django.db import models
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nom du tag")

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Sujet")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(null=True, blank=True, verbose_name="Date de fin")
    
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Tags")
    linked_tasks = models.ManyToManyField(
        'self', 
        blank=True, 
        symmetrical=False, 
        verbose_name="Tâches liées"
    )
    
    controlled = models.TextField(verbose_name="Ce que je contrôle (actions, pensées)")
    uncontrolled = models.TextField(verbose_name="Ce que je ne contrôle pas (résultats externes)")
    corrective_action = models.TextField(verbose_name="Action de correction")

    class Meta:
        ordering = ['-start_date']

    def __str__(self) -> str:
        return self.subject

    def get_absolute_url(self) -> str:
        return reverse('task_list')
