# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TLKdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BoardPositions',
            new_name='BoardPosition',
        ),
        migrations.RenameModel(
            old_name='MeritTypes',
            new_name='CommitteeType',
        ),
        migrations.RenameModel(
            old_name='OfficialTypes',
            new_name='MemberType',
        ),
        migrations.RenameModel(
            old_name='CommitteeTypes',
            new_name='MeritType',
        ),
        migrations.RenameModel(
            old_name='MemberTypes',
            new_name='OfficialType',
        ),
    ]
