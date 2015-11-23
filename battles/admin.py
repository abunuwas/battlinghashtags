from django.contrib import admin

from .models import Tweet, Hashtag, Battle

class BattleAdmin(admin.ModelAdmin):
	fieldsets = [
		('Battle #', {
			'fields': ['id']
			}),
		('Battle date', {
			'fields': ['battle_date']
			}),
		('Winner', {
			'fields': ['winner']
			}),
		('Loser', {
			'fields': ['loser']
			}),
		('Duration', {
			'fields': ['battle_span']
			}),
	]

	list_display = ('id', 'battle_date', 'winner', 'loser')
	list_filter = ['battle_date']




admin.site.register(Battle, BattleAdmin)
admin.site.register(Tweet)
admin.site.register(Hashtag)
