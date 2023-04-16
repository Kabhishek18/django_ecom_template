from django.db import models
from django.urls import reverse



STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class DynamicPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    meta_tag = models.TextField(null=True, default='', blank=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dynamic_page', args=[str(self.id)])
