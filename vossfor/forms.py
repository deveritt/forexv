from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML
from django import forms
from django.forms import Form
from vossfor import constants


class CurrencyConverterFormView(Form):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_class = 'no-asterisk'
        self.helper.form_tag = True
        self.helper.form_method = 'POST'
        self.helper.form_action = ''

        super(CurrencyConverterFormView, self).__init__(*args, **kwargs)

        from_currencies = forms.ChoiceField(
            label="Convert_from:",
            choices=constants.CURRENCIES
        )

        from_amount = forms.FloatField(
            label="",
            min_value=1.00,
            initial=1.00
        )

        self.fields['from_currency'] = from_currencies
        self.fields['from_amount'] = from_amount

        self.helper.layout = Layout(
            'from_currency',
            'from_amount',
            HTML("""<br><button type="submit" class="btn btn-primary">Convert</button>""")
        )
