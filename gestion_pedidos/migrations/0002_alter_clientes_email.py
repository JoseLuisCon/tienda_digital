# Generated by Django 4.2.16 on 2024-09-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestion_pedidos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientes",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]