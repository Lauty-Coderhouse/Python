from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0005_alter_publicacion_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='main_image',
            field=models.ImageField(blank=True, default='post_image/default-post.jpg', null=True, upload_to='post_image'),
        ),
    ]
