from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_name_profile_surname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'País', 'verbose_name_plural': 'Paises'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfiles'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.country'),
        ),
    ]
