# Generated by Django 4.1.1 on 2023-05-20 15:12

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
            name='Vehicle',
            fields=[
                ('vehicle_number', models.CharField(max_length=20)),
                ('vehicle_type', models.CharField(choices=[('Two', 'Two wheelers'), ('Three', 'Three wheelers'), ('Four', 'Four wheelers')], max_length=10)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_description', models.CharField(max_length=300)),
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('superadmin', 'Super admin'), ('admin', 'Admin'), ('user', 'User')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
