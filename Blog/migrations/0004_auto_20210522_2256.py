# Generated by Django 3.2.3 on 2021-05-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Background_Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Image1',
            field=models.ImageField(upload_to=''),
        ),
    ]