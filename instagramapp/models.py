# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Editor(models.Model):
    user_name = models.CharField(max_length = 40)
    user_email = models.CharField(max_length = 40)
    def __str__(self):
        return self.user_name