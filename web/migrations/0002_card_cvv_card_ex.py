# Generated by Django 5.0.3 on 2024-04-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='cvv',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='ex',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]