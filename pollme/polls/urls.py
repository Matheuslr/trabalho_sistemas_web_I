from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('list/', views.polls_list, name = 'list'),
    path('add/', views.add_poll, name = 'add'),
    path('edit/<int:poll_id>', views.edit_poll, name = 'edit_poll'),
    path('edit/<int:poll_id>/choice/add/', views.add_choice, name = 'add_choice'),
    #poll/details/1/
    path('details/<int:poll_id>/', views.polls_detail, name = 'detail'),
    #polls/details/1/vote
    path('details/<int:poll_id>/vote/', views.poll_vote, name = 'vote'),
]
