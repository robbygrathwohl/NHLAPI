from nhl_api.rest_adapter import RestAdapter
from nhl_api.base_models import Player

nhlapi = RestAdapter(hostname='api-web.nhle.com')
result = nhlapi.get('player/8478402/landing')
player = Player(**result.data[0])
print(player.player_id, player.first_name, player.last_name)