# Generated by Django 4.1 on 2023-10-17 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_display', '0003_element_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='element', to='order_display.order'),
        ),
    ]
