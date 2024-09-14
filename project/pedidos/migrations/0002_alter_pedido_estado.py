# Generated by Django 5.1 on 2024-09-14 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'Estado que significa que el pedido aún no ha sido revisado'), ('EN_PROCESO', 'Estado que significa que el pedido está en proceso de revisión'), ('COMPLETADO', 'Estado que significa que el pedido ha sido completado')], default='PENDIENTE', max_length=20),
        ),
    ]
