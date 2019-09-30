# Generated by Django 2.2.3 on 2019-08-30 10:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('treefile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treefile.category')),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treefile.category')),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('content', tinymce.models.HTMLField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treefile.category')),
            ],
        ),
    ]