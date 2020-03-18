from django import forms
from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('user', 'content', 'image')

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 500:
            raise forms.ValidationError('content is too long')
        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content')
        image = data.get('image')
        if content is None and image is None:
            raise forms.ValidationError('Content and image  cannot be both empty')
        return super(StatusForm, self).clean(*args, **kwargs)
