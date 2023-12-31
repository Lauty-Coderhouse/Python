from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0002_publicacion_dt_update_publicacion_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='publicaciones.categoria'),
        ),
    ]
