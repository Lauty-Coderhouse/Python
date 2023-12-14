from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_img_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timezone',
            options={'verbose_name': 'Zona horaria', 'verbose_name_plural': 'Zonas horarias'},
        ),

        migrations.AlterField(
            model_name='profile',
            name='timezone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.timezone'),
        ),
    ]
