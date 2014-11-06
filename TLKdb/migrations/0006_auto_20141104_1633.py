# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TLKdb', '0005_auto_20141104_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('year', models.DateField()),
                ('person', models.ForeignKey(related_name='boards', to='TLKdb.Person')),
                ('type', models.ForeignKey(related_name='boards', to='TLKdb.BoardPosition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('year', models.DateField()),
                ('person', models.ForeignKey(related_name='committees', to='TLKdb.Person')),
                ('type', models.ForeignKey(related_name='committees', to='TLKdb.CommitteeType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('year', models.DateField()),
                ('person', models.ForeignKey(related_name='members', to='TLKdb.Person')),
                ('type', models.ForeignKey(related_name='members', to='TLKdb.MemberType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Merit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('year', models.DateField()),
                ('person', models.ForeignKey(related_name='merits', to='TLKdb.Person')),
                ('type', models.ForeignKey(related_name='merits', to='TLKdb.MeritType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('year', models.DateField()),
                ('person', models.ForeignKey(related_name='officials', to='TLKdb.Person')),
                ('type', models.ForeignKey(related_name='officials', to='TLKdb.OfficialType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='person',
            name='board',
        ),
        migrations.RemoveField(
            model_name='person',
            name='committee',
        ),
        migrations.RemoveField(
            model_name='person',
            name='member',
        ),
        migrations.RemoveField(
            model_name='person',
            name='merit',
        ),
        migrations.RemoveField(
            model_name='person',
            name='official',
        ),
    ]
