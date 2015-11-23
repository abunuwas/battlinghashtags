from django.contrib import admin

from .models import Tweet, Hashtag, Battle, BattleOutcome

class BattleOutcomeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Battle #', {
			'fields': ['battle']
			}),
		('Winner', {
			'fields': ['winner_hashtag']
			}),
		('Loser', {
			'fields': ['loser_hashtag']
			}),
	]

	list_display = ('battle', 'winner_hashtag', 'loser_hashtag')
	#list_filter = ['battle_date']




admin.site.register(BattleOutcome, BattleOutcomeAdmin)
admin.site.register(Battle)
admin.site.register(Tweet)
admin.site.register(Hashtag)
