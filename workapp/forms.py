from django import forms

from .models import Worker, Tools


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('name', 'name_fam', 'years_old',)


class ToolsForm(forms.ModelForm):
    class Meta:
        model = Tools
        fields = ('name', 'worker', 'inv_number', 'cost',)
