from django.db import models

class Battle(models.Model):
	battle_date = models.DateTimeField('date of the battle')
	battle_span = models.IntegerField(default=0)

class Hashtag(models.Model):
	hashtagText = models.CharField(max_length=150)

	def __str__(self):
		return self.hashtagText

class Tweet(models.Model):
	text = models.CharField(max_length=150)
	created_at = models.DateTimeField('created at')
	typos = models.IntegerField(default=0)
	battle = models.ForeignKey(Battle)
	hashtag = models.ForeignKey(Hashtag)

	def __str__(self):
		return self.text

class BattleOutcome(models.Model):
	battle = models.ForeignKey(Battle)
	winner_hashtag = models.ForeignKey(Hashtag, related_name='winner', default=None, blank=True, null=True)
	loser_hashtag = models.ForeignKey(Hashtag, related_name='loser', default=None, blank=True, null=True)
	loser_typos = models.IntegerField(default=0)
	winner_typos = models.IntegerField(default=0)



