
from django.forms import ModelForm
from cms.models import Kanmusu, Impression


class KanmusuForm(ModelForm):
    """艦娘のフォーム"""
    class Meta:
            model = Kanmusu
            fields = ('shipname', 'shipclass', 'shiplevel', )

class ImpressionForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Impression
        fields = ('comment', )

