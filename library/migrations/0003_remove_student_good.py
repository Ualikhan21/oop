# Generated by Django 5.1.6 on 2025-04-04 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_student_good'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='good',
        ),
    ]
