# Generated by Django 3.2.22 on 2023-10-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('descricao', models.TextField()),
                ('local', models.CharField(max_length=50)),
                ('dress_code', models.TextField()),
            ],
        ),
    ]
