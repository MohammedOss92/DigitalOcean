# Generated by Django 4.2 on 2023-09-02 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Img_Api', '0005_delete_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImgeName', models.CharField(max_length=255)),
                ('ImageUrl', models.ImageField(upload_to='images/')),
                ('new_imgs', models.CharField(default=1, max_length=2, null=True)),
                ('ID_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Img_Api.imagetype')),
            ],
        ),
    ]
