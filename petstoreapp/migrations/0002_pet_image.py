# Generated by Django 5.0.2 on 2024-02-25 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pet_images/'),
        ),
    ]
