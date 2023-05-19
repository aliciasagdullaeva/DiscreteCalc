from django import forms
from .models import EqualityCondition


class ConditionForm(forms.Form):
    condition = forms.CharField(label='condition', max_length=64)


class EqualityForm(forms.Form):
    class Meta:
        model = EqualityCondition
        fields = ['firstCondition', 'secondCondition']
        required = {
            'firstCondition': True,
            'secondCondition': True,
        }


class MonotoneForm(forms.Form):
    condition = forms.CharField(label='condition', max_length=255)


class SelfDualityForm(forms.Form):
    condition = forms.CharField(label='condition', max_length=255)


class SheffForm(forms.Form):
    condition = forms.CharField(label='condition', max_length=255)


class SokrDNFForm(forms.Form):
    condition = forms.CharField(label='condition', max_length=255)
