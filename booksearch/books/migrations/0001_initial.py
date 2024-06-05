# Generated by Django 4.2.10 on 2024-05-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=20)),
                ('summary', models.TextField(blank=True, null=True)),
                ('tfidf_vector', models.BinaryField(blank=True, null=True)),
            ],
        ),
    ]