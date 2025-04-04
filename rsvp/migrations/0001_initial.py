# Generated by Django 5.2 on 2025-04-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('is_invited', models.BooleanField(default=True)),
                ('has_rsvped', models.BooleanField(default=False)),
                ('attending', models.BooleanField(blank=True, null=True)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
