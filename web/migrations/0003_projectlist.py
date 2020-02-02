# Generated by Django 2.1.7 on 2019-10-19 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0002_auto_20191019_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order', models.IntegerField(null=True, unique=True)),
                ('project_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]