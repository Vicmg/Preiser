# Generated by Django 2.0.6 on 2018-10-21 21:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20181017_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalle_prestamo',
            old_name='estado',
            new_name='estado_elemento',
        ),
        migrations.RenameField(
            model_name='detalle_prestamo',
            old_name='fecha_entrega',
            new_name='fecha_devolucion',
        ),
        migrations.RenameField(
            model_name='prestamo',
            old_name='catidad',
            new_name='cantidad_total',
        ),
        migrations.RemoveField(
            model_name='detalle_prestamo',
            name='fecha_limite',
        ),
        migrations.RemoveField(
            model_name='detalle_prestamo',
            name='nombre',
        ),
        migrations.AddField(
            model_name='detalle_prestamo',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalle_prestamo',
            name='estado_prestamo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='fecha_entrega',
            field=models.DateField(default=datetime.datetime(2018, 10, 21, 21, 19, 10, 498740, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detalle_prestamo',
            name='descripcion',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_prestamo',
            name='tipo_dano',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
