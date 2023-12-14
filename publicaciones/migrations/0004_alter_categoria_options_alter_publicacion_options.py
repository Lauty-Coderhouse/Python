from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0003_alter_publicacion_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='publicacion',
            options={'verbose_name': 'Publicación', 'verbose_name_plural': 'Publicaciones'},
        ),
    ]
