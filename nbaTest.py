import urllib
from time import sleep
import re
from urllib import request





url = "https://www.espn.com/nba/player/stats/_/id/3975"
f = urllib.request.urlopen(url)
sleep(0.3)
player_source = f.read().decode('utf-8')
# extract career stats using this regex
stats_regex = ('\[\"Career\",\"\",(.*?)\]\},\{\"ttl\"\:\"Regular Season Totals\"')
career_info = re.findall(stats_regex, player_source)
print(career_info)