# Generated by Django 2.2.3 on 2019-07-26 06:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tools',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1),
        ),
    ]
