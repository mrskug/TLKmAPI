# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TLKdb', '0009_person_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.CharField(blank=True, max_length=45, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='company_email',
            field=models.CharField(blank=True, max_length=120, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='company_phone',
            field=models.CharField(blank=True, max_length=45, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, max_length=1000, null=True),
            preserve_default=True,
        ),
    ]
