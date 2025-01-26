from msilib.schema import Component
from nhl_api.convert_result import convert_keys_to_snake_case

class Result:
    def __init__(self, status_code: int, message: str = '', data: list[dict] = None):
        """
            Result returned from low-level RestAdapter
            :param status_code: Standard HTTP Status code
            :param message: Human readable result
            :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.message = str(message)
        # Convert all dictionaries in the data list to have snake_case keys
        if data is None:
            self.data = []
        elif isinstance(data, dict):  # Handle case where a single dictionary is provided
            self.data = [convert_keys_to_snake_case(data)]
        else:
            self.data = [convert_keys_to_snake_case(item) for item in data]


class Player:
    # /v1/player/{player_id}/landing
    def __init__(self, player_id: int, is_active: bool, current_team_id: int, first_name: dict, last_name: dict, sweater_number: int, position: str, featured_stats: dict, career_totals: dict, **kwargs):
        """
            :param playerId: Player ID
            :param is_active: True/False
            :param current_team_id: numerical value by alphabetical order
            :param first_name: eg 'Connor'
            :param last_name: eg 'McDavid'
            :param sweater_number: int value
            :param position: eg 'C'
            :param featured_stats: Dict of 'regular_season' and 'playoffs'
            :param career_totals: Dict of 'regular_season' and 'playoffs'
        """
        self.player_id = int(player_id)
        self.is_active = bool(is_active)
        self.current_team_id = int(current_team_id)
        self.first_name = str(first_name['default'])
        self.last_name = str(last_name['default'])
        self.sweater_number = int(sweater_number)
        self.position = str(position)
        self.featured_stats = dict(featured_stats)
        self.career_totals = dict(career_totals)
        self.extra_attributes = kwargs

'''class PlayerGameLog:
    # /v1/player/{player_id}/game-log/{season}/{game-type}
    def __init__(self, player_id: int, season: int, game_type: int, data: list[dict] = None):
        """
            :param player_id: Player ID
            :param season: Season in YYYYYYYY format, where the first four digits represent the start year of the season, and the last four digits represent the end year.
            :param game_type: Game type (guessing 2 for regular season, 3 for playoffs)
            :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.player_id = int(player_id)
        self.season = int(season)
        self.game_type = int(game_type)'''




'''class PlayerSpotlight:
    #v1/player-spotlight
    def __init__():'''

'''
class Schedule:
    #v1/schedule
    def __init__():'''

'''class SeasonStandings:
    #v1/standings-season
    def __init__():'''

'''class SchedulePlayoffSeries:
    #v1/schedule/playoff-series
    def __init__():'''

'''class Score:
    # v1/score
    def __init__():'''

'''class Location:
    #v1/location
    def __init__():'''
'''
class Season:
    #v1/season
    def __init__():'''

'''class SkaterStatsLeaders
    #v1/skater-stats-leaders
    def __init__():'''

'''class WhereToWatch:
    #v1/where-to-watch
    def __init__():'''

'''class ClubStats:
    #v1/club-stat
    def __init__():
'''
'''class Prospects:
    #v1/prospects
    def __init__():'''

'''class PostalLookup:
    #/v1/postal-lookup
    def __init__():'''

'''class ClubScheduleSeason:
    #v1/club-schedule-season
    def __init__():'''

'''class PlayoffSeries:
    #v1/playoff-series
    def __init__():'''

'''class DraftTrackers:
    #v1/draft-tracker
    def __init__():'''

'''class DraftPicks:
    #/v1/draft/picks
    def __init__():'''

'''class Scoreboard:
    #v1/scoreboard
    def __init__():'''

'''class Roster:
    #v1/roster
    def __init__():'''

'''class ClubSchedule:
    #v1/club-schedule
    def __init__():'''

'''class PPTReplay:
    #v1/ppt-replay
    def __init__():'''

'''class Standings:
    #v1/standings
    def __init__():'''



'''class RosterSeason:
    #v1/roster-season
    def __init__():'''

'''class GameCenter:
    #v1/gamecenter
    def __init__():'''

'''class Meta:
    #v1/meta
    def __init__():'''

'''class WSCGameStory:
    #v1/wsc/game-story
    def __init__():'''

'''class GoalieStatsLeaders:
    #v1/goalie-stats-leaders
    def __init__():'''

'''class DraftRankings:
    #v1/draft/rankings
    def __init__():'''

'''class PlayoffBracket:
    #v1/playoff-bracket
    def __init__():'''

'''class PartnerGame
    #v1/partner-game/{country-code}/now
    def __init__():'''

'''class Network:
    #v1/network
    def __init__():'''

'''class ScheduleCalendar:
    #v1/schedule-calendar
    def __init__():'''

'''class ClubStatsSeason:
    #v1/club-stats-season
    def __init__():'''