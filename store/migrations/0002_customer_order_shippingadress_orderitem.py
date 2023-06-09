# Generated by Django 4.2 on 2023-04-18 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='true', max_length=200, null='true')),
                ('email', models.CharField(blank='true', max_length=200, null='true')),
                ('user', models.OneToOneField(blank='true', null='true', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(blank='true', max_length=200, null='true')),
                ('completed', models.BooleanField(null='true')),
                ('customer', models.ForeignKey(blank='true', null='true', on_delete=django.db.models.deletion.SET_NULL, to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank='true', max_length=200, null='true')),
                ('customer', models.OneToOneField(blank='true', null='true', on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('order', models.OneToOneField(blank='true', null='true', on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(blank='true', default=0, null='true')),
                ('order', models.ForeignKey(blank='true', null='true', on_delete=django.db.models.deletion.SET_NULL, to='store.order')),
                ('product', models.ForeignKey(blank='true', null='true', on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
        ),
    ]
