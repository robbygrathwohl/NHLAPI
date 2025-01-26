from dataclasses import dataclass
from typing import Optional, List, Dict
from datetime import datetime
from enum import Enum


@dataclass
class FullTeamName:
    default: str
    fr: Optional[str] = None


@dataclass
class Award:
    trophy: FullTeamName
    seasons: List[Dict[str, int]]


@dataclass
class Badge:
    logo_url: FullTeamName
    title: FullTeamName


@dataclass
class BirthCity:
    default: str


@dataclass
class Playoffs:
    assists: int
    game_winning_goals: int
    games_played: int
    goals: int
    ot_goals: int
    pim: int
    plus_minus: int
    points: int
    power_play_goals: int
    power_play_points: int
    shooting_pctg: float
    shorthanded_goals: int
    shorthanded_points: int
    shots: int
    avg_toi: Optional[str] = None
    faceoff_winning_pctg: Optional[float] = None


@dataclass
class CareerTotals:
    regular_season: Playoffs
    playoffs: Playoffs


@dataclass
class FirstName:
    default: str
    cs: Optional[str] = None
    fi: Optional[str] = None
    sk: Optional[str] = None


@dataclass
class CurrentTeamRoster:
    player_id: int
    last_name: BirthCity
    first_name: FirstName
    player_slug: str


@dataclass
class DraftDetails:
    year: int
    team_abbrev: str
    round: int
    pick_in_round: int
    overall_pick: int


@dataclass
class RegularSeason:
    sub_season: Playoffs
    career: Playoffs


@dataclass
class FeaturedStats:
    season: int
    regular_season: RegularSeason


@dataclass
class Last5Game:
    assists: int
    game_date: datetime
    game_id: int
    game_type_id: int
    goals: int
    home_road_flag: str
    opponent_abbrev: str
    pim: int
    plus_minus: int
    points: int
    power_play_goals: int
    shifts: int
    shorthanded_goals: int
    shots: int
    team_abbrev: str
    toi: str


class Fr(Enum):
    OILERS_D_EDMONTON = "Oilers d'Edmonton"


@dataclass
class TeamName:
    default: str
    cs: Optional[str] = None
    de: Optional[str] = None
    es: Optional[str] = None
    fi: Optional[str] = None
    sk: Optional[str] = None
    sv: Optional[str] = None
    fr: Optional[Fr] = None


@dataclass
class SeasonTotal:
    assists: int
    game_type_id: int
    games_played: int
    goals: int
    league_abbrev: str
    points: int
    season: int
    sequence: int
    team_name: TeamName
    pim: Optional[int] = None
    game_winning_goals: Optional[int] = None
    plus_minus: Optional[int] = None
    power_play_goals: Optional[int] = None
    shorthanded_goals: Optional[int] = None
    shots: Optional[int] = None
    team_common_name: Optional[TeamName] = None
    team_place_name_with_preposition: Optional[FullTeamName] = None
    avg_toi: Optional[str] = None
    faceoff_winning_pctg: Optional[float] = None
    ot_goals: Optional[int] = None
    power_play_points: Optional[int] = None
    shooting_pctg: Optional[float] = None
    shorthanded_points: Optional[int] = None


@dataclass
class Player:
    player_id: int
    is_active: bool
    current_team_id: int
    current_team_abbrev: str
    full_team_name: FullTeamName
    team_common_name: BirthCity
    team_place_name_with_preposition: FullTeamName
    first_name: BirthCity
    last_name: BirthCity
    badges: List[Badge]
    team_logo: str
    sweater_number: int
    position: str
    headshot: str
    hero_image: str
    height_in_inches: int
    height_in_centimeters: int
    weight_in_pounds: int
    weight_in_kilograms: int
    birth_date: datetime
    birth_city: BirthCity
    birth_state_province: BirthCity
    birth_country: str
    shoots_catches: str
    draft_details: DraftDetails
    player_slug: str
    in_top100_all_time: int
    in_hhof: int
    featured_stats: FeaturedStats
    career_totals: CareerTotals
    shop_link: str
    twitter_link: str
    watch_link: str
    last5_games: List[Last5Game]
    season_totals: List[SeasonTotal]
    awards: List[Award]
    current_team_roster: List[CurrentTeamRoster]
