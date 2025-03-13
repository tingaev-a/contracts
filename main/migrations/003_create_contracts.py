from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main', '002_create_reference_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(primary_key=True)),
                ('counterparty1', models.CharField(max_length=200)),
                ('counterparty2', models.CharField(max_length=200)),
                ('signing_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('subject', models.TextField()),
                ('one_time_cost', models.DecimalField(max_digits=10, decimal_places=2)),
                ('periodic_cost', models.DecimalField(max_digits=10, decimal_places=2)),
                ('additional_terms', models.TextField()),
                ('user', models.ForeignKey('User', on_delete=models.CASCADE)),
                ('status', models.ForeignKey('Status', on_delete=models.CASCADE)),
                ('counterparty_type', models.ForeignKey('CounterpartyType', on_delete=models.CASCADE)),
                ('currency', models.ForeignKey('Currency', on_delete=models.CASCADE)),
            ],
        ),
    ]