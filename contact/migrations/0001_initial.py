# Generated by Django 5.0.6 on 2024-10-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=15)),
                ('mensaje', models.TextField()),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
                ('tipo_pedido', models.CharField(choices=[('EV', 'Evento'), ('TI', 'Tienda'), ('RE', 'Restaurante')], default='EV', max_length=2)),
                ('estado', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
            ],
        ),
    ]
