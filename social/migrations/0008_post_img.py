# Generated by Django 3.2.9 on 2021-12-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='zamieszczane/zdj_posty'),
        ),
    ]
