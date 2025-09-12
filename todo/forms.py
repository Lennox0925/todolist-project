from django.forms import ModelForm
from.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "important","date_completed"]
        # fields = "__all__"