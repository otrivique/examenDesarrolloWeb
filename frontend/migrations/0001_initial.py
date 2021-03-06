# Generated by Django 3.1.4 on 2020-12-16 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rutUsuario', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Rut usuario')),
                ('nombreUsuario', models.CharField(max_length=50, verbose_name='Nombre usuario')),
                ('claveUsuario', models.CharField(max_length=20, verbose_name='Clave usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID producto')),
                ('nombreProducto', models.CharField(max_length=50, verbose_name='Nombre producto')),
                ('descripcionProducto', models.CharField(max_length=200, verbose_name='Descripcion producto')),
                ('cantidadProducto', models.IntegerField(verbose_name='Cantidad producto')),
                ('fechRegProducto', models.DateTimeField(verbose_name='Fecha de registro')),
                ('categoriaProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.categoria')),
            ],
        ),
    ]
