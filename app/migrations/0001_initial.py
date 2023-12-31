# Generated by Django 4.2.2 on 2023-07-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=60, null=True)),
                ('password', models.CharField(max_length=12, null=True)),
                ('gender', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100, null=True)),
                ('resume', models.FileField(null=True, upload_to='')),
                ('img', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='File_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='media')),
            ],
        ),
    ]
