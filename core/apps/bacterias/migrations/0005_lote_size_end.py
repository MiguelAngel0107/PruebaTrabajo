# Generated by Django 4.2.2 on 2023-07-03 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bacterias", "0004_lote_id_collection"),
    ]

    operations = [
        migrations.AddField(
            model_name="lote",
            name="size_end",
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
