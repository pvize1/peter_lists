from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
from .models import Book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "subtitle",
            "tag",
            "slug",
            "description",
            "author",
            "publisher",
            "type",
            "form",
            "status",
        ]

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        # self.helper.form_class = "form-horizontal"
        # self.helper.label_class = "col-sm-2"
        # self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            Fieldset(
                "ABOUT",
                Row(
                    Column("title", css_class="form-group col-sm"),
                    Column("tag", css_class="form-group col-sm"),
                    # css_class='form-row'
                ),
                Row(
                    Column("subtitle", css_class="form-group col-sm"),
                    Column("slug", css_class="form-group col-sm"),
                    # css_class='form-row'
                ),
            ),
            "description",
            Fieldset(
                "DETAILS",
                Row(
                    Column("author", css_class="form-group col-sm"),
                    Column("publisher", css_class="form-group col-sm"),
                    # css_class='form-row'
                ),
                Row(
                    Column("type", css_class="form-group col-sm"),
                    Column("form", css_class="form-group col-sm"),
                    # css_class='form-row'
                ),
            ),
            Submit('submit', 'Save Book')
        )
        self.request = kwargs.pop("request", None)
        return super(CreateBookForm, self).__init__(*args, **kwargs)
