# Generated by Django 3.2.4 on 2021-06-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_app_app_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='app_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]