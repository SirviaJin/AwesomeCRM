# Generated by Django 2.1.1 on 2018-11-03 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0008_remove_course_course_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyrecord',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='repository.Course'),
            preserve_default=False,
        ),
    ]
