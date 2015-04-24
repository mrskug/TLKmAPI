# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TLKdb', '0008_auto_20150204_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=45, null=True),
            preserve_default=True,
        ),
    ]
