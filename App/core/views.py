from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView, FormView
from App.core.models import Pais

class IndexView(TemplateView):
    template_name = 'index.html'

#class RedirectView(TemplateView):
 #   template_name = 'redierct.html'


class PaisesListView(ListView):
    model = Pais
    template_name = 'paises_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'Listado de Paises'
        return context