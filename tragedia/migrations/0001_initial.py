# Generated by Django 4.1.7 on 2023-03-20 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.TextField(max_length=10000)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('articulo', models.ManyToManyField(to='tragedia.articulo')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tragedia.autor'),
        ),
    ]