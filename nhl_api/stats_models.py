from msilib.schema import Component


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
        self.data = data if data else []

'''class Config:
    # en/config
    def __init__():'''

'''class Goalie:
    # en/Goalie
    def __init__():'''

'''class LeadersGoalies:
    # en/leaders/goalies/{attribute}
    def __init__():'''

'''class LeadersSkaters:
    # en/leaders/skaters/{attribute}
    def __init__():'''

'''class ComponentSeason:
    # en/componentSeason
    def __init__():'''

'''class Season:
    # en/season
    def __init__():'''

'''class Country:
    # en/country
    def __init__():'''

'''class Game:
    # en/game
    def __init__():'''

'''class Glossary:
    # en/glossary
    def __init__():'''

'''class MilestonesSkaters:
    # en/milestones/skaters
    def __init__():'''

'''class Team:
    # en/team
    def __init__():'''

'''class Skater:
    # en/skater

    def __init__():'''

'''class MilestoneGoalies:
    # en/milestones/goalies
    def __init__():'''


'''class Draft:
    # en/Draft
    def __init__():'''

'''class Players:
    # en/players
    def __init__():'''

'''class Shiftcharts:
    # en/shiftcharts
    def __init__():'''

'''class ContentModule:
    # en/content/module
    def __init__():'''

'''class Franchise:
    def __init__():'''