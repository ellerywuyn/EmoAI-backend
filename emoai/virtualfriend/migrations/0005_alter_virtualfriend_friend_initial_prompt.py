# Generated by Django 4.2.7 on 2023-12-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualfriend', '0004_virtualfriend_friend_mbti_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualfriend',
            name='friend_initial_prompt',
            field=models.TextField(blank=True, null=True),
        ),
    ]