from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Blog


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title",
            "description",
            "date",
            "tag",
        ]

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        # self.helper.form_class = "form-horizontal"
        # self.helper.label_class = "col-sm-2"
        # self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            "title",
            "description",
            "date",
            "tag",
            Submit('submit', 'Save Blog Entry')
        )
        self.request = kwargs.pop("request", None)
        return super(EditBlogForm, self).__init__(*args, **kwargs)
