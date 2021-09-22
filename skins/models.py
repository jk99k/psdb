from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

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
    motif = models.CharField(max_length=64, blank=True, null=True)

    like_count = models.IntegerField(default=0)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # PS3D
    skin_id = models.CharField(max_length=16)
    image = models.ImageField(upload_to=get_skin_image_path)

    def __str__(self):
        return str(self.skin_id)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skin = models.ForeignKey(Skin, on_delete=models.CASCADE)

    def __str__(self):
        return ("{} => {}".format(self.user, self.skin))