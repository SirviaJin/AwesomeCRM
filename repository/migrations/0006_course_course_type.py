# Generated by Django 2.1.1 on 2018-11-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20181101_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.SmallIntegerField(choices=[(0, '面授'), (1, '脱产'), (2, '周末'), (3, '网络')], default=1, verbose_name='课程类型'),
            preserve_default=False,
        ),
    ]