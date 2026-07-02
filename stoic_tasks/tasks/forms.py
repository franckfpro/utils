from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'subject', 'start_date', 'end_date', 'tags', 
            'linked_tasks', 'controlled', 'uncontrolled', 'corrective_action'
        ]
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Application des classes Tailwind à tous les champs
        css_class = "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border"
        for field in self.fields.values():
            field.widget.attrs['class'] = css_class
        
        # Widgets spécifiques pour les dates
        self.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date', 'class': css_class})
        self.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date', 'class': css_class})
