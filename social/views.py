from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.djhtml'

class TestPage(TemplateView):
    template_name = 'test.djhtml'

class ThanksPage(TemplateView):
    template_name = 'thanks.djhtml'

