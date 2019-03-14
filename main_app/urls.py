from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.players_index, name='index'),
    path('players/<int:player_id>/', views.players_detail, name='detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'),
    path('players/<int:player_id>/add_healing/', views.add_healing, name='add_healing'),
    path('players/<int:player_id>/assoc_sneaker/<int:sneaker_id>/', views.assoc_sneaker, name='assoc_sneaker'),
    path('players/<int:player_id>/unassoc_sneaker/<int:sneaker_id>/', views.unassoc_sneaker, name='unassoc_sneaker'),
    path('sneakers/', views.SneakerList.as_view(), name='sneakers_index'),
    path('sneakers/<int:pk>/', views.SneakerDetail.as_view(), name='sneaker_detail'),
    path('sneakers/create/', views.SneakerCreate.as_view(), name='sneakers_create'),
    path('sneakers/<int:pk>/update/', views.SneakerUpdate.as_view(), name='sneakers_update'),
    path('sneakers/<int:pk>/delete/', views.SneakerDelete.as_view(), name='sneakers_delete'),
]