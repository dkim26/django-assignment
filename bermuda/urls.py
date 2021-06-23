from django.urls import path

from . import views

app_name = 'bermuda'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('new', views.CreateView.as_view(), name='create'),
  path('anime', views.AnimeView.as_view(), name='anime'),
  path('comic', views.ComicView.as_view(), name='comic'),
  path('film', views.FilmView.as_view(), name='film'),
  path('drama', views.DramaView.as_view(), name='drama'),
  path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
  path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
  path('<int:question_id>/vote/', views.vote, name='vote')
]

