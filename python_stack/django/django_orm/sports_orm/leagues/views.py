from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues":League.objects.filter(sport__icontains = 'baseball'),
		"womens_leagues":League.objects.filter(name__icontains = 'women'),
		"hockey_leagues":League.objects.filter(sport__icontains = 'hockey'),
		"not_football":League.objects.exclude(sport__icontains = 'football'),
		"conferences":League.objects.filter(name__icontains = 'conference'),
		"atlantic_region":League.objects.filter(name__icontains = 'atlantic'),
		"dallas":Team.objects.filter(location__icontains = 'dallas'),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")