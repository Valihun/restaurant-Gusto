# Generated by Django 3.1.5 on 2021-02-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_gusto', '0008_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='discription',
            field=models.CharField(max_length=300, null=True),
        ),
    ]