from django.db import models

# Create your models here.
class StrategyInst(models.Model):
    
    id = models.AutoField(primary_key=True)
    config  = models.JSONField()
    enabled = models.BooleanField(default=True)
    class Meta:
        db_table = 'strategy_inst'
        verbose_name = '策略实例'
        verbose_name_plural = '策略实例'
        managed =False