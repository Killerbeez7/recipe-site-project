# Generated by Django 3.1.3 on 2022-04-17 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0003_auto_20220415_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='RecipeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='recipes')),
                ('is_selected', models.BooleanField(default=False)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_app.recipe')),
            ],
        ),
    ]
