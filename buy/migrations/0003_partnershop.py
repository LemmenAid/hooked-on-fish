# Generated by Django 3.2.25 on 2025-03-04 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_buyinperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
                ('buy_in_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_shops', to='buy.buyinperson')),
            ],
        ),
    ]
