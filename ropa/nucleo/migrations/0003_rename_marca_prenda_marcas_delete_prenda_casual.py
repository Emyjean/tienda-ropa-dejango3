# Generated by Django 4.1.5 on 2023-02-02 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nucleo", "0002_alter_marca_options_alter_prenda_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="prenda",
            old_name="marca",
            new_name="marcas",
        ),
        migrations.DeleteModel(
            name="prenda_casual",
        ),
    ]
