from django.db import models

STATUS_LS_CHOICES = [
    ('Have to do', 'have_to_do'),
    ('In process', 'in_process'),
    ('Done', 'done')
]

class Tasks(models.Model):
    title = models.TextField(max_length=3500, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=3500, null=True, blank=True, verbose_name='Description')
    status = models.TextField(max_length=50, null=False, blank=False, choices=STATUS_LS_CHOICES, default='have_to_do', verbose_name='Status')
    created_at = models.DateField(auto_now=False, null=True, blank=True, verbose_name='Date of done')
