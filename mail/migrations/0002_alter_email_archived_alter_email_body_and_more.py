# Generated by Django 4.2.3 on 2025-01-31 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='archived',
            field=models.BooleanField(default=False, help_text='Indica se o e-mail foi arquivado.'),
        ),
        migrations.AlterField(
            model_name='email',
            name='body',
            field=models.TextField(blank=True, help_text='Corpo do e-mail.'),
        ),
        migrations.AlterField(
            model_name='email',
            name='read',
            field=models.BooleanField(default=False, help_text='Indica se o e-mail foi lido.'),
        ),
        migrations.AlterField(
            model_name='email',
            name='recipients',
            field=models.ManyToManyField(help_text='Usuários que recebem o e-mail.', related_name='emails_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='email',
            name='sender',
            field=models.ForeignKey(help_text='Usuário que enviou o e-mail.', on_delete=django.db.models.deletion.PROTECT, related_name='emails_sent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='email',
            name='subject',
            field=models.CharField(help_text='Assunto do e-mail.', max_length=255),
        ),
        migrations.AlterField(
            model_name='email',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, help_text='Data e hora em que o e-mail foi enviado.'),
        ),
        migrations.AlterField(
            model_name='email',
            name='user',
            field=models.ForeignKey(help_text='Usuário proprietário da caixa de entrada.', on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL),
        ),
    ]
