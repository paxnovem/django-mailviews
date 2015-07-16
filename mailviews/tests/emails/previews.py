import random

from django import forms

from mailviews.previews import Preview, site
from mailviews.tests.emails.views import (BasicEmailMessageView,
    BasicHTMLEmailMessageView)


class BasicPreview(Preview):
    message_view = BasicEmailMessageView
    verbose_name = 'Basic Message'
    description = 'A basic text email message.'

    def get_message_view(self, request):
        subject = ('''Robot ipsum datus scan amet, constructor ad ut splicing 
         elit, sed do errus mod tempor in conduit ut laboratory et deplore
         electromagna aliqua. Ut enim ad minimum veniam, quis no indestruct
         exoform ullamco laboris nisi ut alius equip ex ea commando evaluant.
         Duis ex machina aute ire dolorus in scan detectus an voluptate volt
         esse cesium dolore eu futile nulla parameter. Execute primus sint
         occaecat cupidatat non proident, sunt in culpa qui technia deserunt
         mondus anim id est proceus.''')
        content = ('''\n Robot ipsum Calciolite misoplex teloene xanthphobe
          ossidrome auriculomania sexiatric Arabobiosis bartomy. Warcele
          heliotherm holophobic hematocele exbitropic gynase septuaphage
          yobiiatrics. Luteoscript underscopy xeroese homeometry
          parthenophilous gynotropy homolatry hendecaales. Bathourous
          aleuroeaux basidom egoably Indoemia parilogue Araboic. Indoathon
          selenogate spirohood hieroistical gastrograph autcentric butyroeaux
          trisity combioideae myescent. Mangamous sphagia spondylopara
          psychroplasia arnophilia adenorama ventrigene leptomorphic.''')
        return self.message_view(subject, content)


class BasicHTMLPreview(BasicPreview):
    message_view = BasicHTMLEmailMessageView
    verbose_name = 'Basic HTML Message'
    description = 'A basic HTML email message.'


class CustomizationForm(forms.Form):
    subject = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    def get_message_view_kwargs(self):
        return self.cleaned_data


class CustomizablePreview(Preview):
    message_view = BasicEmailMessageView
    verbose_name = 'Basic Message, with Form'
    description = 'A basic text email message, but customizable.'
    form_class = CustomizationForm


site.register(BasicPreview)
site.register(BasicHTMLPreview)
site.register(CustomizablePreview)
