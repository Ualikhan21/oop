# Generated by Django 5.1.7 on 2025-03-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=20, unique=True)),
                ('year', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('access', models.BooleanField())
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('borrowed_books', models.ManyToManyField(blank=True, to='library.book')),
            ],
        ),
    ]
