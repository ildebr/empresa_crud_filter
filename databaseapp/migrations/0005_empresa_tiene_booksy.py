# Generated by Django 4.2 on 2023-05-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseapp', '0004_empresa_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='tiene_booksy',
            field=models.BooleanField(default=False),
        ),
    ]