# Generated by Django 4.2.1 on 2023-05-31 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='snippet.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'snippet',
            },
        ),
    ]
