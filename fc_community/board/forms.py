from django import forms


class BoardForm(forms.Form):
  title = forms.CharField(
    error_messages={
      'required': 'Please Input Title.'
    },
    max_length=128, label="Title")
  contents = forms.CharField(
    error_messages={
      'required': 'Please Write Articles.'
    },
    widget=forms.Textarea, label="Adticle")

  tags = forms.CharField(
    required=False, label='Tag')
