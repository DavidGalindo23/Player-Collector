from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player
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
    healing_form = HealingForm()
    return render(request, 'players/detail.html', { 'player': player, 'healing_form': healing_form })

def add_healing(request, player_id):
    form = HealingForm(request.POST)
    if form.is_valid: 
        new_healing = form.save(commit=False)
        new_healing.player_id = player_id
        new_healing.save()
    return redirect('detail', player_id=player_id)