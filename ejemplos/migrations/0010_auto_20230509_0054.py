# Generated by Django 2.0.2 on 2023-05-09 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplos', '0009_auto_20230508_2326'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Proveedor',
        ),
        migrations.AlterField(
            model_name='producto',
            name='proveedor',
            field=models.ManyToManyField(to='prov.Proveedor'),
        ),
    ]