# Generated by Django 5.0.4 on 2024-10-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='image_url',
            field=models.URLField(max_length=1500),
        ),
    ]