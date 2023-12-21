from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)

class AddAnimeForm(forms.Form):
    Name = forms.CharField(label='Name', max_length=200)
    Aired = forms.CharField(label='Aired', max_length=200)
    Studios = forms.CharField(label='Studios', max_length=200)
    Description = forms.CharField(label='Description')
    Image = forms.CharField(label='Image')
    Video = forms.CharField(label='Video')
    Type = forms.CharField(label='Type')

class DeleteAnimeForm(forms.Form):
    id = forms.HiddenInput()

from .models import Comment
from mptt.forms import TreeNodeChoiceField


class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ('name', 'parent', 'email', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'email': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(NewCommentForm, self).save(*args, **kwargs)