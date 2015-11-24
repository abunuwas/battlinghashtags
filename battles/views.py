from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader 
from django.core.urlresolvers import reverse 

from .models import Battle, Hashtag, Tweet, BattleOutcome

from .twitter_streaming import *
from .twitter_analyzer import twitterAnalyzer


def index(request):
	latest_battle_list = BattleOutcome.objects.all()
	for battle in latest_battle_list:
		print(battle)
		battle.winner_tweets = len(battle.winner_hashtag.tweet_set.filter(battle=battle.battle.id))
		battle.loser_tweets = len(battle.loser_hashtag.tweet_set.filter(battle=battle.battle.id))
		#battle.winner = Hashtag.objects.get(pk=battle.winner_hashtag.id).hashtagText
		#battle.loser = Hashtag.objects.get(pk=battle.loser_hashtag.id).hashtagText
		#battle.battle_date = battle.
		#battle.span = Battle.objects.get(pk=battle.battle.id).battle_span
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

		try:
			hashtag1 = Hashtag.objects.get(hashtagText=hashtag1_text)
		except Hashtag.DoesNotExist: 
			hashtag1 = Hashtag(hashtagText = hashtag1_text)
			hashtag1.save()

		try:
			hashtag2 = Hashtag.objects.get(hashtagText=hashtag2_text)
		except Hashtag.DoesNotExist: 
			hashtag2 = Hashtag(hashtagText = hashtag2_text)
			hashtag2.save()

		newBattle = Battle(battle_date = timezone.now(), battle_span = 30)
		newBattle.save()
		battle_id = newBattle.id

		print('Listening to the twitter stream')
		twitter_stream = Stream(auth, MyListener(hashtag1=hashtag1, 
			hashtag2=hashtag2, battle=newBattle, time_span=newBattle.battle_span))
		hashtags = hashtag1_text + ', ' + hashtag2_text
		print(hashtags)
		twitter_stream.filter(track=[hashtags])

		hashtag1_count = len(hashtag1.tweet_set.filter(battle=battle_id))
		hashtag2_count = len(hashtag2.tweet_set.filter(battle=battle_id))
		hashtags = {hashtag1_count: hashtag1, hashtag2_count: hashtag2}
		winner = max(hashtags)
		loser = min(hashtags)
		
		newBattleOutcome = BattleOutcome(battle=newBattle, 
											winner_hashtag=hashtags[winner],
											loser_hashtag =hashtags[loser]
											)

		newBattleOutcome.save()

	except KeyError:
		return render(request, 'battles/addBattle.html')
	except:
		raise
		return render(request, 'battles/addBattle.html')
	else:
		return HttpResponseRedirect(reverse('battles:index'))

