# Generated by Django 5.0.2 on 2024-02-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('idPaquete', models.AutoField(primary_key=True, serialize=False)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dimensiones', models.CharField(max_length=50)),
                ('direccion_origen', models.CharField(max_length=255)),
                ('direccion_destino', models.CharField(max_length=255)),
                ('estado_entrega', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Transportista',
            fields=[
                ('idTransportista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_vehiculo', models.CharField(max_length=50)),
                ('numero_contacto', models.CharField(max_length=20)),
            ],
        ),
    ]
