# # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Image,Profile
import datetime as dt


# # Create your tests here.
class ImageTestClass(TestCase):
    #set up method

    def test_save_method(self):
        self.image.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        self.image.delete_image()
        self.objects.filter(image=image).delete()
        self.assertTRue(len(images)>0)

