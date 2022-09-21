from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = {'message': 'hello'}
        return context