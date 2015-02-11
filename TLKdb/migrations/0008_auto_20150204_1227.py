# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TLKdb', '0007_auto_20141106_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='year',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
