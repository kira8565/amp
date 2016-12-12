from django import forms
from django.forms import TextInput
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe


class HpInputWidget(forms.widgets.TextInput):
    def __init__(self, attrs={}):
        super(HpInputWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)

        if value != '':
            final_attrs['value'] = self._format_value(value)

        return mark_safe('<div class="form-group"><input%s class="form-control"></div>' % flatatt(final_attrs))
