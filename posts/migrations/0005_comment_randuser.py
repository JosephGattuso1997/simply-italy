# Generated by Django 3.2.5 on 2021-08-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_gallary'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='randUser',
            field=models.CharField(default='Anonymous User', max_length=20),
            preserve_default=False,
        ),
    ]
