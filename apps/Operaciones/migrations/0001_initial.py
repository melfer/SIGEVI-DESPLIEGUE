# Generated by Django 4.1.7 on 2023-09-10 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Gestion', '0001_initial'),
        ('Personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(default='root', max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('total', models.IntegerField(default=0)),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Personas.cliente')),
            ],
            options={
                'verbose_name': 'Cotizacion',
                'verbose_name_plural': 'Cotizaciones',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(default='root', max_length=50)),
                ('total', models.IntegerField(default=0)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Personas.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('subtotal', models.IntegerField(default=0)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Gestion.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operaciones.venta')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('subtotal', models.IntegerField(default=0)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operaciones.cotizacion')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Gestion.producto')),
            ],
            options={
                'verbose_name': 'DetalleCotizacion',
                'verbose_name_plural': 'DetallesCotizaciones',
            },
        ),
    ]
