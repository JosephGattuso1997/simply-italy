# Generated by Django 3.2.5 on 2021-08-05 17:28

from django.db import migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='thumbnail',
            field=smartfields.fields.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallary',
            name='thumbnail',
            field=smartfields.fields.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=smartfields.fields.ImageField(upload_to=''),
        ),
    ]