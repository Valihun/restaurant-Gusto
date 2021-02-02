# Generated by Django 3.1.5 on 2021-02-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_gusto', '0004_banners_is_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=200)),
                ('is_processed', models.BooleanField(default=False)),
                ('send_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
