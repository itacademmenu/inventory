import uuid
from django.db import models
from django.urls import reverse


class Worker(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, default=uuid.uuid1)
    name_fam = models.CharField(max_length=50)
    years_old = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        reverse('tools_list', args=[{'slug': self.slug}])


class Tools(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, default=uuid.uuid1)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='tools')
    inv_number = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return self.name

