# Generated by Django 3.2.19 on 2023-05-26 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0004_alter_cotizacion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]