# Generated by Django 4.2.1 on 2023-05-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='img',
            field=models.ImageField(default=1234, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
