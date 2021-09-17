from django.db import models

from users.models import User

import os
import uuid


class Skin(models.Model):

    def get_skin_image_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (uuid.uuid4(), ext)
        return os.path.join('skins/images/', filename)

    SKIN_TYPE_CHOICES = (
        ('1', 'Low res'),
        ('2', 'High res')
    )

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256, blank=True, null=True)
    skin_type = models.CharField(choices=SKIN_TYPE_CHOICES, max_length=1)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # PS3D
    skin_id = models.CharField(max_length=16)
    image = models.ImageField(upload_to=get_skin_image_path)

    def __str__(self):
        return str(self.skin_id)