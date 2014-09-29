# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class RunMetadata(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    key = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)
    run = models.ForeignKey('Runs')

    class Meta:
        managed = False
        db_table = 'run_metadata'


class Runs(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    skips = models.IntegerField(blank=True, null=True)
    fails = models.IntegerField(blank=True, null=True)
    passes = models.IntegerField(blank=True, null=True)
    run_time = models.FloatField(blank=True, null=True)
    artifacts = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'runs'


class TestMetadata(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    key = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)
    test_run = models.ForeignKey('Tests')

    class Meta:
        managed = False
        db_table = 'test_metadata'


class TestRunMetadata(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    key = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)
    test_run = models.ForeignKey('TestRuns')

    class Meta:
        managed = False
        db_table = 'test_run_metadata'


class TestRuns(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    test = models.ForeignKey('Tests')
    run = models.ForeignKey(Runs)
    status = models.CharField(max_length=256, blank=True)
    start_time = models.DateTimeField(blank=True, null=True)
    stop_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_runs'


class Tests(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    test_id = models.CharField(max_length=256)
    run_count = models.IntegerField(blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    failure = models.IntegerField(blank=True, null=True)
    run_time = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tests'
