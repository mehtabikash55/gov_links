# Generated by Django 4.0.6 on 2022-09-20 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0006_social_media_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='gov_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Website_Title', models.CharField(max_length=50)),
                ('Website_Link', models.CharField(max_length=100)),
            ],
        ),
    ]
