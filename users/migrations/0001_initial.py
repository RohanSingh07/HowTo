# Generated by Django 3.2.3 on 2021-05-21 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='last_joined')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
