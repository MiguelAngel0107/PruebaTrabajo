# Generated by Django 4.2.2 on 2023-07-02 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bacterias", "0002_lote"),
    ]

    operations = [
        migrations.AddField(
            model_name="lote",
            name="nivel_iter",
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]