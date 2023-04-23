from django.db import models
from django.urls import reverse
from django.utils.text import slugify



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
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    debug_switch = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('dynamic_page', args=[str(self.slug)])

