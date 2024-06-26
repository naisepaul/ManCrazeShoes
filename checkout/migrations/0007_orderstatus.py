# Generated by Django 4.2.11 on 2024-06-29 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='in_progress', max_length=200, null=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
            ],
        ),
    ]
