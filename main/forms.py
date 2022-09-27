from django import forms


class ConditionForm(forms.Form):
    condition = forms.CharField(label='condition', max_length=64)
