# Generated by Django 3.1.2 on 2022-06-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.FloatField(primary_key=True, serialize=False)),
                ('detalle_boleta', models.CharField(max_length=100)),
                ('valor_boleta', models.FloatField()),
            ],
            options={
                'db_table': 'boleta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('rut', models.FloatField()),
                ('dv_rut', models.CharField(max_length=1)),
                ('fechar_registro', models.DateField()),
                ('deuda', models.FloatField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CodigoBarra',
            fields=[
                ('id_codigo_barra', models.FloatField(primary_key=True, serialize=False)),
                ('img_codigo', models.BinaryField()),
            ],
            options={
                'db_table': 'codigo_barra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('nc', models.FloatField(primary_key=True, serialize=False)),
                ('fecha_comprobante', models.CharField(max_length=50)),
                ('valor', models.FloatField()),
            ],
            options={
                'db_table': 'comprobante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id_detalle', models.FloatField(primary_key=True, serialize=False)),
                ('numboleta', models.FloatField()),
                ('producto', models.FloatField()),
                ('cantidad', models.FloatField()),
                ('precio', models.FloatField()),
            ],
            options={
                'db_table': 'detalle_boleta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apelido_paterno', models.FloatField()),
                ('apellido_materno', models.FloatField()),
                ('rut', models.FloatField()),
                ('dv_rut', models.CharField(max_length=1)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.FloatField()),
                ('fecha_contrato', models.CharField(max_length=50)),
                ('fecha_termino_contrato', models.CharField(blank=True, max_length=50, null=True)),
                ('cargo', models.CharField(max_length=50)),
                ('sueldo', models.FloatField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fiado',
            fields=[
                ('id_fiado', models.FloatField(primary_key=True, serialize=False)),
                ('monto', models.FloatField()),
                ('plazo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'fiado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id_informe', models.FloatField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'informe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdenPedido',
            fields=[
                ('id_orden', models.FloatField(primary_key=True, serialize=False)),
                ('detalle_orden', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'orden_pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PagoFiado',
            fields=[
                ('id_pago', models.FloatField(primary_key=True, serialize=False)),
                ('estado_pago', models.CharField(max_length=1)),
                ('valor_abono', models.FloatField()),
            ],
            options={
                'db_table': 'pago_fiado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.FloatField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('fecha_vencimiento', models.DateField()),
                ('stock', models.FloatField()),
                ('barcode', models.FloatField()),
                ('img_producto', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=50)),
                ('rubro', models.CharField(max_length=50)),
                ('telefono', models.FloatField()),
                ('correo', models.CharField(max_length=50)),
                ('id_informe', models.FloatField()),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecepcionProducto',
            fields=[
                ('id_recepcion', models.FloatField(primary_key=True, serialize=False)),
                ('detalle_recepcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'recepcion_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo_producto', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_tipo', models.CharField(max_length=50)),
                ('img_tipo', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tipo_producto',
                'managed': False,
            },
        ),
    ]
