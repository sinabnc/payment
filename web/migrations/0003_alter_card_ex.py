# Generated by Django 5.0.3 on 2024-04-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_card_cvv_card_ex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='ex',
            field=models.TextField(max_length=33),
        ),
    ]
