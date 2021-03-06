# Generated by Django 2.2.2 on 2019-06-25 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=48)),
                ('title', models.CharField(max_length=48)),
                ('content', models.TextField(max_length=65535)),
                ('tag', models.CharField(max_length=48)),
                ('firsttime', models.DateTimeField(auto_now_add=True)),
                ('lasttime', models.DateTimeField(auto_now_add=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'content',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=48)),
                ('email', models.CharField(max_length=48)),
                ('password', models.CharField(max_length=128)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('idDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
