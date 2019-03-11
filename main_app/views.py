from django.shortcuts import render
from django.http import HttpResponse


class Player: 
    def __init__(self, name, age, team, position, jerseyNumber):
        self.name = name
        self.age = age
        self.team = team
        self.position = position
        self.jerseyNumber = jerseyNumber

players = [ 
    Player('Kyrie Irving', 23, 'Boston Celtics', 'PG', 11 ),
    Player('Russell WesBrook', 30, 'Oklahoma City Thunder', 'PG', 10 ),
    Player('Paul George', 28,'Oklahoma City Thunder', 'SF', 13),
    Player('James Harden', 29, 'Houston Rockets', 'SG', 13),
    Player('Joel Embiid', 24, 'Philadelphia 76ers', 'C', 21)
] 



# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello Player</h1>')

def about(request):
    return render(request, 'about.html')

def players_index(request):
    return render(request, 'players/index.html', {'players': players })
