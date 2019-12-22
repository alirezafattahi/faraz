# Generated by Django 3.0.1 on 2019-12-19 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20191219_0349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'قرارداد', 'verbose_name_plural': 'قراردادها'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'مشتری', 'verbose_name_plural': 'مشتریان'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'کارمند', 'verbose_name_plural': 'کارمندان'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'خدمت', 'verbose_name_plural': 'خدمات'},
        ),
        migrations.AlterModelOptions(
            name='recive_cheque',
            options={'verbose_name': 'چک', 'verbose_name_plural': 'چک های دریافتی'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(help_text='نام', max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(help_text='نام', max_length=30),
        ),
        migrations.AlterField(
            model_name='recive_cheque',
            name='cheque_amount',
            field=models.BigIntegerField(verbose_name='مبلغ چک'),
        ),
        migrations.AlterField(
            model_name='recive_cheque',
            name='status',
            field=models.CharField(choices=[('w', 'در انتظار وصول'), ('p', 'وصول شد'), ('i', 'برگشت خورد'), ('r', 'در انتظار دریافت')], max_length=1),
        ),
        migrations.CreateModel(
            name='karbarg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_date', models.DateField()),
                ('cash_pay', models.BigIntegerField()),
                ('description', models.TextField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.contract')),
                ('person_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.person')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.product')),
            ],
            options={
                'verbose_name': 'کاربرگ',
                'verbose_name_plural': ' کاربرگ ها',
            },
        ),
    ]