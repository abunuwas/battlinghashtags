from django.db import models

class Hashtag(models.Model):
	tweet = models.ForeignKey(Tweet)
	hashtagText = models.CharField(max_length=150)

	def __str__(self):
		return self.hashtagText

class HastagTypo(models.Model):
	hashtag = models.ForeignKey(Hashtag)
	typos = models.IntegerField(default=0)

class Battle(models.Model):
	winner = models.ForeignKey(Hashtag, related_name='hashtag_winner', default=None, blank=True, null=True)
	loser = models.ForeignKey(Hashtag, related_name='hashtag_loser', default=None, blank=True, null=True)
	battle_date = models.DateTimeField('date of the battle')
	battle_span = models.IntegerField(default=0)

class Tweet(models.Model):
	text = models.CharField(max_length=150)
	created_at = models.DateTimeField('created at')
	typos = models.IntegerField(default=0)
	battle = models.ForeignKey(Battle)

	def __str__(self):
		return self.text

