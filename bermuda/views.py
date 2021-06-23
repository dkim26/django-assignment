from django.views import generic
from django.urls import reverse_lazy
from .models import Bermuda, Question

class IndexView(generic.ListView):
  template_name = 'bermuda/index.html'
  context_object_name = 'bermuda_list'

  def get_queryset(self):
    """Return all ."""
    return Bermuda.objects.all()
    return Question.objects.order_by('-pub_date')[:5]

class CreateView(generic.edit.CreateView):
  template_name = 'bermuda/create.html'
  model = Bermuda
  fields = ['message']
  success_url = reverse_lazy('bermuda:index')

class AnimeView(generic.ListView):
  template_name = 'bermuda/anime.html'
  model = Bermuda
  fields = ['message']
  success_url = reverse_lazy('bermuda:anime')

class ComicView(generic.ListView):
  template_name = 'bermuda/comic.html'
  model = Bermuda
  fields = ['message']
  success_url = reverse_lazy('bermuda:comic')

class FilmView(generic.ListView):
  template_name = 'bermuda/film.html'
  model = Bermuda
  fields = ['message']
  success_url = reverse_lazy('bermuda:film')
 
class DramaView(generic.ListView):
  template_name = 'bermuda/drama.html'
  model = Bermuda
  fields = ['message']
  success_url = reverse_lazy('bermuda:drama')

class UpdateView(generic.edit.UpdateView):
    template_name = 'bermuda/update.html'
    model = Bermuda
    fields = ['message']
    success_url = reverse_lazy('bermuda:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'bermuda/delete.html'
    model = Bermuda
    success_url = reverse_lazy('bermuda:index')
       
class DetailView(generic.DetailView):
    model = Question
    template_name = 'bermuda/detail.html'
def vote(request, question_id):
    ... # same as above, no changes needed.

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'bermuda/results.html'



