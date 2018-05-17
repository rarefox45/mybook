from django.db import models

# Create your models here.


class Kanmusu(models.Model):
    """艦娘"""
    shipname = models.CharField('艦名', max_length=255)
    shipclass = models.CharField('艦種', max_length=255, blank=True)
    shiplevel = models.IntegerField('レベル', blank=True, default=1)

    def __str__(self):
        return self.shipname


class Impression(models.Model):
    """個人的萌えポイント"""
    ship = models.ForeignKey(Kanmusu, verbose_name="艦娘", related_name='impressions', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment
