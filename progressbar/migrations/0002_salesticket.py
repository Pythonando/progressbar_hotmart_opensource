# Generated by Django 5.2 on 2025-05-06 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progressbar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=255)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='progressbar.batch')),
            ],
        ),
    ]
