# -*- coding: utf-8 -*-
from pyscada.models import Variable,BackgroundTask

from django.db import models
from django.contrib.auth.models import User
#
# Model
#

class ScheduledExportTask(models.Model):
    id 				= models.AutoField(primary_key=True)
    label			= models.CharField(max_length=400, default='')
    variables		= models.ManyToManyField(Variable)
    day_time_choices = [(x,'%d:00'%x) for x in range(0,24)]
    day_time        = models.PositiveSmallIntegerField(default=0,choices=day_time_choices,help_text='day time wenn the job will start be started')
    mean_value_period = models.PositiveSmallIntegerField(default=0,help_text='in Seconds (0 = no mean value)')
    active		    = models.BooleanField(default=False,blank=True,  help_text='to activate scheduled export')
    file_format_choises = (('hdf5','Hierarchical Data Format Version 5'),('mat','Matlab® mat v7.3 compatible file'),('CSV_EXCEL','Microsoft® Excel® compatible csv file'))
    file_format     = models.CharField(max_length=400, default='hdf5',choices=file_format_choises)
    export_period_choises = ((1,'1 Day'),(2,'2 Days (on every even Day of the year)'),(7,'7 Days (on Mondays)'),(14,'14 Days'),(30,'30 Days'))
    export_period = models.PositiveSmallIntegerField(default=0,choices=export_period_choises,help_text='')
    def __unicode__(self):
        return unicode(self.label)


class ExportTask(models.Model):
    id 				= models.AutoField(primary_key=True)
    label			= models.CharField(max_length=400, default='')
    backgroundtask	= models.ForeignKey(BackgroundTask,null=True, on_delete=models.SET_NULL)
    variables		= models.ManyToManyField(Variable)
    mean_value_period = models.PositiveSmallIntegerField(default=0,help_text='in Seconds (0 = no mean value)')
    file_format_choises = (('hdf5','Hierarchical Data Format Version 5'),('mat','Matlab® mat v7.3 compatible file'),('CSV_EXCEL','Microsoft® Excel® compatible csv file'))
    file_format     = models.CharField(max_length=400, default='hdf5',choices=file_format_choises)
    time_min        = models.FloatField(default=None, null=True,blank=True)
    time_max        = models.FloatField(default=None, null=True,blank=True)
    user	 		= models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    start 			= models.FloatField(default=0)
    fineshed		= models.FloatField(default=0,blank=True)
    done			= models.BooleanField(default=False,blank=True)
    failed			= models.BooleanField(default=False,blank=True)
    def __unicode__(self):
        return unicode(self.label)