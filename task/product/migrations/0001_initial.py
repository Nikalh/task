# Generated by Django 4.1.7 on 2023-04-23 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('factory', '0001_initial'),
        ('retail', '__first__'),
        ('network', '0001_initial'),
        ('entrepreneur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('debt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='factory.factory')),
                ('individual_entrepreneur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='entrepreneur.individualentrepreneur')),
                ('network_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='network.networknode')),
                ('retail_network', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='retail.retailnetwork')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
