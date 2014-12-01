# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TLKdb', '0006_auto_20141104_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='year',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='committee',
            name='year',
            field=models.IntegerField(max_length=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='year',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='merit',
            name='year',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='official',
            name='year',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
