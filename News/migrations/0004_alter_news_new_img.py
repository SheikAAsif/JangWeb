# Generated by Django 4.1.7 on 2023-04-29 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_news_new_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='new_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='New_img/'),
        ),
    ]
