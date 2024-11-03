from django import forms


class EmailContentForm(forms.Form):
    subject = forms.CharField(label="Assunto")
    content = forms.CharField(widget=forms.Textarea, label="Conteúdo do email")
    
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
