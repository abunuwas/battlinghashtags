from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader 
from django.core.urlresolvers import reverse 

from .models import Battle, Hashtag, Tweet

from .twitter_streaming import *
from .twitter_analyzer import twitterAnalyzer


def index(request):
	latest_battle_list = Battle.objects.order_by('-battle_date')[:10]
	for battle in latest_battle_list:
		battle.winner = Hashtag.objects.get(pk=battle.winner).text
		battle.loser = Hashtag.objects.get(pk=battle.loser).text
	context = {'latest_battle_list': latest_battle_list}
	return render(request, 'battles/index.html', context)

def addBattle(request):
	try:
		hashtag1_text = request.POST['hashtag1']
		hashtag2_text = request.POST['hashtag2']
		if not hashtag1_text.startswith('#'):
			hashtag1_text = '#'+hashtag1_text
		if not hashtag2_text.startswith('#'):
			hashtag2_text = '#'+hashtag2_text
		print(hashtag1_text, hashtag2_text)

		hashtag1 = Hashtag(hashtagText = hashtag1_text)
		hashtag2 = Hashtag(hashtagText = hashtag2_text)
		newBattle = Battle(battle_date = timezone.now(), battle_span = 20)
		battle_id = newBattle.id

		print('Listening to the twitter stream')
		twitter_stream = Stream(auth, MyListener(hashtag1=hashtag1, 
			hashtag2=hashtag2, battle_id=battle_id))
		twitter_stream.filter(track=[hashtag1_text + ' ' + hashtag2_text])
		


	except KeyError:
		return render(request, 'battles/addBattle.html')
	except:
		raise
		return render(request, 'battles/addBattle.html')
	else:
		return HttpResponseRedirect(reverse('battles:index'))

