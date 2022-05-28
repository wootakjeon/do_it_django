from django import forms
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget
from .models import Comment
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


class BoardWriteForm(forms.ModelForm):
    title = forms.CharField(
        label='게시글 제목:',
        
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목을 입력해 주세요.'
            }),
        required=True,
    )

    text = SummernoteTextField()

    field_order = [
        'title',
        'text',
        'photo'
    ]

    class Meta:
        model = Post
        fields = [
            'title',
            'text'
        ]
        widgets = {
            'text': SummernoteWidget()
        }

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        text = cleaned_data.get('text', '')

        if title == '':
            self.add_error('title', "글 제목을 입력하세요. ")
        elif text == '':
            self.add_error('text', '글 내용을 입력하세요.')
        else:
            self.title = title
            self.text = text


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
