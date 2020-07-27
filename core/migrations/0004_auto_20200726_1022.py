# Generated by Django 3.0.8 on 2020-07-26 13:22

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200726_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-layers', 'Design'), ('lni-cog', 'Engrenagem'), ('lni-users', 'Usuários'), ('lni-stats-up', 'Gráfico'), ('lni-mobile', 'Mobile')], max_length=12, verbose_name='Ícone'),
        ),
    ]