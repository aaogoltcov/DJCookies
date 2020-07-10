from django.contrib import admin
from django.forms import BaseInlineFormSet

from game.models import Player, Game, PlayerGameInfo


class RelationshipInlineFormset(BaseInlineFormSet):
    pass


class RelationshipInline(admin.TabularInline):
    model = PlayerGameInfo
    formset = RelationshipInlineFormset


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


# @admin.register(PlayerGameInfo)
# class PlayerGameInfoAdmin(admin.ModelAdmin):
#     inlines = [RelationshipInline]





