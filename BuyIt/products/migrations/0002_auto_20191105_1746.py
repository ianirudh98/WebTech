# Generated by Django 2.2.5 on 2019-11-05 17:46

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10, unique=True)),
                ('shop_slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Shop',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('sub_category', models.CharField(max_length=20)),
                ('category_slug', models.SlugField(blank=True, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Shop')),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='all', on_delete=django.db.models.deletion.CASCADE, to='products.Product_Category'),
        ),
    ]
