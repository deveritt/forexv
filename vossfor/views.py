from django.views.generic import FormView, TemplateView
from vossfor.forms import CurrencyConverterFormView
from django.urls import reverse
from django.contrib import messages
from vossfor.api import ForexConvert
from vossfor.constants import BASE


class ForexConverterView(FormView):

    template_name = 'index.html'
    form_class = CurrencyConverterFormView
    result = ''

    def get_success_url(self):

        return reverse('result', kwargs={'result': self.result})

    def form_valid(self, form):

        try:

            amount = float(form.data.get('from_amount', 1.00))
            base_currency = BASE[int(form.data.get('from_currency', 0))]
            converter = ForexConvert()
            zars = converter.do_conversion(currency_code=base_currency, amount=amount)
            self.result = "ZAR {:.2f}".format(zars)

        except Exception as e:

            # Log the error and make it user friendly.
            # messages.error(self.request, e) # haven't set this up either
            self.result = "Unable to convert currency."

        finally:

            return super(ForexConverterView, self).form_valid(form)


class ConverterResultView(TemplateView):

    template_name = 'result.html'
