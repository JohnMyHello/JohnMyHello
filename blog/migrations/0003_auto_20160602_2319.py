# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160530_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='uesrname',
            new_name='username',
        ),
    ]
