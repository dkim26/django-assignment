from django.views import generic
from django.urls import reverse_lazy
from .models import Bermuda

class IndexView(generic.ListView):
  template_name = 'bermudas/index.html'
  context_object_name = 'bermuda_list'

  def get_queryset(self):
    """Return all ."""
    return Bermuda.objects.all()

class CreateView(generic.edit.CreateView):
  template_name = 'bermudas/create.html'
  model = Bermuda
  fields = ['message']
  success_url = reverse_lazy('bermudas:index')

class UpdateView(generic.edit.UpdateView):
    template_name = 'bermudas/update.html'
    model = Bermuda
    fields = ['message']
    success_url = reverse_lazy('bermudas:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'bermudas/delete.html'
    model = Bermuda
    success_url = reverse_lazy('bermudas:index')

