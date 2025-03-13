from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main', '003_create_contracts'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(primary_key=True)),
                ('file', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('document_type', models.ForeignKey('DocumentType', on_delete=models.CASCADE)),
                ('contract', models.ForeignKey('Contract', on_delete=models.CASCADE)),
            ],
        ),
    ]