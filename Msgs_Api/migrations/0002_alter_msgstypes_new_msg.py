# Generated by Django 4.1.1 on 2022-11-22 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Msgs_Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgstypes',
            name='new_msg',
            field=models.CharField(default=1, max_length=2),
        ),
    ]