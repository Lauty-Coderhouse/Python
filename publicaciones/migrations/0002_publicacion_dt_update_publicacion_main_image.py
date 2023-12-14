from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='dt_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='post_image'),
        ),
    ]
