# Generated by Django 3.0.7 on 2021-02-15 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('delivery_at', models.DateTimeField()),
                ('address', models.CharField(max_length=256)),
                ('status', models.CharField(choices=[('created', 'готов'), ('delivered', 'доставлен'),
                                                     ('processed', 'обрабатывается'), ('cancelled', 'отмене')],
                                            max_length=50)),
                ('total_cost', models.DecimalField(decimal_places=2, default=True, max_digits=13)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders',
                                           to='carts.Cart')),
            ],
        ),
    ]
