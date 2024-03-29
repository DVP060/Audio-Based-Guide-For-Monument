# Generated by Django 4.1.3 on 2023-03-07 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('audioguideapp', '0022_remove_audio_monument_id_delete_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=15)),
                ('popular_place', models.ImageField(null=True, upload_to='city')),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='monument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monument_name', models.CharField(max_length=30)),
                ('name_guj', models.CharField(max_length=30)),
                ('name_hindi', models.CharField(max_length=30)),
                ('info_eng', models.TextField()),
                ('info_guj', models.TextField()),
                ('info_hindi', models.TextField()),
                ('charges', models.IntegerField()),
                ('photo', models.ImageField(upload_to='photos')),
                ('address', models.TextField()),
                ('address_guj', models.TextField()),
                ('address_hindi', models.TextField()),
                ('contact_no', models.BigIntegerField()),
                ('timing', models.CharField(max_length=30)),
                ('days', models.CharField(max_length=30)),
                ('map_link', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audioguideapp.category')),
                ('cityid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audioguideapp.city')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=20)),
                ('mobile_no', models.IntegerField()),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')], max_length=6, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('propic', models.ImageField(null=True, upload_to='users')),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('payment_type', models.CharField(choices=[('debit card', 'Debit Card'), ('credit card', 'Credit Card'), ('bank transfer', 'Bank Transfer')], max_length=15)),
                ('receipt_id', models.IntegerField()),
                ('monument_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audioguideapp.monument')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audioguideapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField()),
                ('photo', models.ImageField(null=True, upload_to='users')),
                ('monument_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audioguideapp.monument')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audioguideapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path_eng', models.FileField(null=True, upload_to='files')),
                ('file_path_guj', models.FileField(null=True, upload_to='files')),
                ('file_path_hindi', models.FileField(null=True, upload_to='files')),
                ('monument_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audioguideapp.monument')),
            ],
        ),
    ]
