# Generated by Django 2.2.3 on 2019-08-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_post_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, upload_to='profile-pics'),
        ),
    ]
