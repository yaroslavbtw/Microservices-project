# Generated by Django 4.1.7 on 2023-03-18 23:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_remove_products_recipes_recipes_composition'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModal',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('weight', models.IntegerField()),
                ('product_uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.products')),
            ],
        ),
        migrations.AlterField(
            model_name='recipes',
            name='composition',
            field=models.ManyToManyField(to='Products.productmodal'),
        ),
    ]
