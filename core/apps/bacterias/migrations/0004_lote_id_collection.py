# Generated by Django 4.2.2 on 2023-07-02 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bacterias", "0003_lote_nivel_iter"),
    ]

    operations = [
        migrations.AddField(
            model_name="lote",
            name="id_collection",
            field=models.CharField(default=0, max_length=999),
            preserve_default=False,
        ),
    ]
