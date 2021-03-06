# Generated by Django 3.2 on 2021-05-07 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CCTSAssistanceRequired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('active', models.BooleanField(choices=[(True, True), (False, False)], default=1)),
            ],
            options={
                'verbose_name': 'CCTS Assistance Required',
                'verbose_name_plural': 'CCTS Assistance Required',
            },
        ),
        migrations.CreateModel(
            name='ClosingLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('active', models.BooleanField(choices=[(True, True), (False, False)], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('active', models.BooleanField(choices=[(True, True), (False, False)], default=1)),
            ],
            options={
                'verbose_name': 'Complaint Language',
                'verbose_name_plural': 'Complaint Language',
            },
        ),
        migrations.CreateModel(
            name='CustomerAssistanceRequired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('active', models.BooleanField(choices=[(True, True), (False, False)], default=1)),
            ],
            options={
                'verbose_name': 'Customer Assistance Required',
                'verbose_name_plural': 'Customer Assistance Required',
            },
        ),
        migrations.CreateModel(
            name='ObjectionAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('active', models.BooleanField(choices=[(True, True), (False, False)], default=1)),
            ],
            options={
                'verbose_name': 'Objection Assessment',
                'verbose_name_plural': 'Objection Assessment',
            },
        ),
        migrations.CreateModel(
            name='ObjectionStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(choices=[(True, True), (False, False)], default=1)),
            ],
            options={
                'verbose_name': 'Objection Status',
                'verbose_name_plural': 'Objection Status',
            },
        ),
        migrations.CreateModel(
            name='ReferencedCodeSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('active', models.BooleanField(choices=[(True, True), (False, False)], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(choices=[(True, True), (False, False)], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='StatusNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(choices=[(True, True), (False, False)], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Objection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_id', models.CharField(max_length=10)),
                ('date_submitted', models.DateTimeField()),
                ('date_processing_start', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('date_processing_end', models.DateTimeField(blank=True, null=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objections.agent')),
                ('ccts_assessment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objections.objectionassessment')),
                ('ccts_assistance_required', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objections.cctsassistancerequired')),
                ('ccts_determination_referenced_code_section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ReferencedCodeSectionCCTS', to='objections.referencedcodesection')),
                ('closing_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objections.closinglevel')),
                ('complaint_language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objections.complaintlanguage')),
                ('customer_assistance_required', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objections.customerassistancerequired')),
                ('objection_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objections.objectionstatus')),
                ('psp_objection_referenced_code_section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ReferencedCodeSectionPSP', to='objections.referencedcodesection')),
                ('service_provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objections.serviceprovider')),
                ('status_note', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objections.statusnote')),
            ],
        ),
    ]
