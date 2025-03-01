# Generated by Django 5.1.1 on 2024-10-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_userprofile_avatar_userprofile_bio_alter_tour_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
