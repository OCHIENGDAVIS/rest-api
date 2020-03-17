from django.conf import settings
from django.db import models
from django.core.serializers import serialize


def upload_update_image(instane, filename):
    return f'updates/{instane.user}/{filename}'


class UpdateQuerySetManager(models.QuerySet):
    def serialize(self):
        qs = self
        return serialize('json', qs, fields=('id', 'content', 'image'))


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySetManager(self.model, using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_update_image, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = UpdateManager()

    def __str__(self):
        return self.content or ''

    def serialize(self):
        return serialize('json', [self], fields=('id', 'content', 'image'))
