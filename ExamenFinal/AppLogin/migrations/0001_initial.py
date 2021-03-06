# Generated by Django 3.2.7 on 2021-09-28 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=255)),
                ('rol', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('destino', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
                ('fechain', models.DateField()),
                ('fechafn', models.DateField()),
                ('user', models.ManyToManyField(related_name='travels', to='AppLogin.User')),
            ],
        ),
    ]
