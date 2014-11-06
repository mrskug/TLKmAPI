# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TLKdb', '0002_auto_20141104_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='birthplace',
            field=models.CharField(blank=True, max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(blank=True, max_length=180),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.CharField(blank=True, max_length=45),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='company_email',
            field=models.CharField(blank=True, max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='company_phone',
            field=models.CharField(blank=True, max_length=45),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.CharField(blank=True, max_length=45),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='dod',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='graduated',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='joined',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='middlenames',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='zip',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
    ]
