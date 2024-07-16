from typing import Any
from .models import Task
from django.forms import ModelForm,Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "content",
        ]
    def clean(self) -> dict[str, Any]:
        clean_data = super().clean()
        title = clean_data.get("title")
        content = clean_data.get('content')
        return clean_data
    
