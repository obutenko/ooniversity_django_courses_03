# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '__first__'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(null=True, related_name='assistant_courses', blank=True, to='coaches.Coach'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(null=True, related_name='coach_courses', blank=True, to='coaches.Coach'),
            preserve_default=True,
        ),
    ]
