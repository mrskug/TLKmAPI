# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TLKdb', '0003_auto_20141104_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('year', models.DateField()),
                ('id_person', models.ForeignKey(related_name='person', to='TLKdb.Person')),
                ('id_type', models.ForeignKey(related_name='member_type', to='TLKdb.MemberType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
