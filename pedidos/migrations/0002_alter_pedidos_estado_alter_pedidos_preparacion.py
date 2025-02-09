# Generated by Django 5.0.4 on 2024-04-10 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'pendiente'), ('entregado', 'entregado')], default='pendiente', max_length=10),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='preparacion',
            field=models.CharField(choices=[('lv', 'llevar'), ('rs', 'consumir en restaurante')], default='rs', max_length=20),
        ),
    ]
