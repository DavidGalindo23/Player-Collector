from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import *
from .forms import HealingForm




class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['age', 'team', 'jerseyNumber']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def players_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', {'players': players })

def players_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    sneakers_player_doesnt_have = Sneaker.objects.exclude(id__in= player.sneakers.all().values_list('id'))
    healing_form = HealingForm()
    return render(request, 'players/detail.html', { 'player': player, 'healing_form': healing_form, 'sneakers': sneakers_player_doesnt_have })

def add_healing(request, player_id):
    form = HealingForm(request.POST)
    if form.is_valid: 
        new_healing = form.save(commit=False)
        new_healing.player_id = player_id
        new_healing.save()
    return redirect('detail', player_id=player_id)

def assoc_sneaker(request, player_id, sneaker_id):
    Player.objects.get(id=player_id).sneakers.add(sneaker_id)
    return redirect('detail', player_id=player_id)

def unassoc_sneaker(request, player_id, sneaker_id):
    Player.objects.get(id=player_id).sneakers.remove(sneaker_id)
    return redirect('detail', player_id=player_id)

class SneakerList(ListView):
    model = Sneaker

class SneakerDetail(DetailView):
    model = Sneaker

class SneakerCreate(CreateView):
    model = Sneaker
    fields = '__all__'

class SneakerUpdate(UpdateView):
    model = Sneaker
    fields = ['name', 'color']

class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/sneakers/'
