# Generated by Django 4.2.2 on 2023-07-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bacterias", "0006_lote_nivel_iter_end"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lote",
            name="nivel_iter_end",
            field=models.CharField(default="0", max_length=4),
        ),
    ]
