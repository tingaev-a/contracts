from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main', '001_create_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(primary_key=True)),
                ('role_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(primary_key=True)),
                ('status_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CounterpartyType',
            fields=[
                ('id', models.BigAutoField(primary_key=True)),
                ('type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(primary_key=True)),
                ('type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(primary_key=True)),
                ('currency_code', models.CharField(max_length=3)),
            ],
        ),
    ]