# Generated by Django 4.2.4 on 2023-08-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='title',
            field=models.CharField(default='No title', max_length=256),
        ),
    ]
