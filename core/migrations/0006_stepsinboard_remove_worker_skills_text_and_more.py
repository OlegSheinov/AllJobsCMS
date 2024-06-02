# Generated by Django 5.0.6 on 2024-06-02 13:59

import core.models.snippets.rank
import core.models.snippets.steps_in_board
import django.db.models.deletion
import uuid
import wagtail.fields
import wagtail.snippets.blocks
import wagtail_color_panel.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_worker_skills_text_alter_worker_stack'),
        ('wagtaildocs', '0013_delete_uploadeddocument'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StepsInBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('sort_order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Сортировка')),
                ('is_default', models.BooleanField(blank=True, default=False, help_text='Новым заявкам будет проставляться данный шаг (если не указан какой-либо другой)', verbose_name='Является шагом по-умолчанию')),
                ('is_hidden', models.BooleanField(blank=True, default=False, help_text='Данный шаг (статус) не будет отображаться на доске. Заявкам можно проставить его чтобы скрыть их с доски', verbose_name='Скрыть шаг (статус) на доске')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='worker',
            name='skills_text',
        ),
        migrations.RemoveField(
            model_name='stacktags',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='stacktags',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='stack',
        ),
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.AlterModelOptions(
            name='rank',
            options={},
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='databases_text',
            new_name='databases',
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='other_technologies_text',
            new_name='other_technologies',
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='programming_languages_text',
            new_name='programming_languages',
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='software_development_text',
            new_name='software_development',
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='technologies_text',
            new_name='technologies',
        ),
        migrations.AddField(
            model_name='worker',
            name='skills',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Навыки'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=wagtail.fields.RichTextField(blank=True, max_length=1000, verbose_name='Описание проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Состав команды'),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Технологии проекта'),
        ),
        migrations.AlterField(
            model_name='rank',
            name='color',
            field=wagtail_color_panel.fields.ColorField(max_length=7),
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(blank=True, help_text='Пример: "Kokoc.tech | Java/Middle/2400"', max_length=255, verbose_name='Название запроса')),
                ('uuid', models.UUIDField(default=uuid.uuid4, verbose_name='UUID запроса')),
                ('company_name', models.CharField(max_length=255, verbose_name='Заказчик')),
                ('stack', models.TextField(max_length=2000, verbose_name='Стек')),
                ('rate', models.IntegerField(blank=True, null=True, verbose_name='Рейт покупки')),
                ('project_name', models.CharField(blank=True, max_length=255, verbose_name='Название проекта')),
                ('project_description', wagtail.fields.RichTextField(blank=True, max_length=3000, verbose_name='Описание проекта')),
                ('project_term', models.CharField(blank=True, max_length=255, verbose_name='Срок проекта')),
                ('workers', wagtail.fields.StreamField([('worker', wagtail.snippets.blocks.SnippetChooserBlock('core.Worker'))], blank=True, null=True, verbose_name='Работник')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='Активный')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='demands', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер')),
                ('rank', models.ForeignKey(blank=True, default=core.models.snippets.rank.Rank.get_default_rank, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='demands', to='core.rank', verbose_name='Ранг заявки')),
                ('specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.specialization', verbose_name='Специализация')),
                ('status', models.ForeignKey(default=core.models.snippets.steps_in_board.StepsInBoard.get_default_board, on_delete=django.db.models.deletion.CASCADE, to='core.stepsinboard', verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('telegram_nickname', models.CharField(max_length=255, verbose_name='Telegram')),
                ('company_name', models.CharField(blank=True, max_length=255, verbose_name='Название компании')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='Активный')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document')),
                ('demand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='core.demand')),
            ],
            options={
                'verbose_name': 'Кандидат',
                'verbose_name_plural': 'Кандидаты',
            },
        ),
        migrations.CreateModel(
            name='DemandTimeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_start', models.DateTimeField(auto_now_add=True, verbose_name='Начало')),
                ('status_end', models.DateTimeField(blank=True, null=True, verbose_name='Конец')),
                ('total_seconds', models.BigIntegerField(blank=True, default=0, verbose_name='Суммарная длительность')),
                ('demand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timelogs', to='core.demand', verbose_name='Запрос')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='timelogs', to='core.stepsinboard', verbose_name='Статус')),
            ],
        ),
        migrations.DeleteModel(
            name='SkillsTags',
        ),
        migrations.DeleteModel(
            name='StackTags',
        ),
        migrations.AddField(
            model_name='worker',
            name='stack',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Стек'),
        ),
    ]