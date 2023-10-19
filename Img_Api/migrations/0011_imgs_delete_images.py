# Generated by Django 4.2 on 2023-09-21 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Img_Api', '0010_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='')),
                ('new_img', models.CharField(default=1, max_length=2, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('ID_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Img_Api.imagetype')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
