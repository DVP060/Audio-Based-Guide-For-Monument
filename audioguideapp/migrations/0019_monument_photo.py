# Generated by Django 4.1.3 on 2023-03-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioguideapp', '0018_remove_monument_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='monument',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
    ]
