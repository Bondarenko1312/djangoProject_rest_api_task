# Generated by Django 4.1.1 on 2022-09-16 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='restaurant/menu/%Y/%m/%d')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('restaurant',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_menu',
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
