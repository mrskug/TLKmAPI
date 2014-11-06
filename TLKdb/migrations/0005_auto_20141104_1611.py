# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TLKdb', '0004_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='id_person',
        ),
        migrations.RemoveField(
            model_name='member',
            name='id_type',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AddField(
            model_name='person',
            name='board',
            field=models.ManyToManyField(to='TLKdb.BoardPosition'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='committee',
            field=models.ManyToManyField(to='TLKdb.CommitteeType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='member',
            field=models.ManyToManyField(to='TLKdb.MemberType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='merit',
            field=models.ManyToManyField(to='TLKdb.MeritType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='official',
            field=models.ManyToManyField(to='TLKdb.OfficialType'),
            preserve_default=True,
        ),
    ]
