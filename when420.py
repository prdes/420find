#when420.py

from supybot.utils.str import format
import datetime
from dateutil import parser, tz
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim

# input location

user_location = input('Enter your location: ')

# convert location to timezone
geolocator = Nominatim(user_agent="irc_bot_coordinate_finder")
location = geolocator.geocode(user_location)
tf = TimezoneFinder()
latitude, longitude = location.latitude, location.longitude
timezone = tf.timezone_at(lng=longitude, lat=latitude)

# Convert timezone to aware datetimes and timedeltas
now = datetime.datetime.now(tz=tz.gettz(timezone))

today_420 = now.replace(hour=4, minute=20, second=0, tzinfo=tz.gettz(timezone))
today_1620 = now.replace(hour=16, minute=20, second=0, tzinfo=tz.gettz(timezone))


timezone_code = today_420.tzname()

twelve_td = datetime.timedelta(hours= 12)
zero_td = datetime.timedelta()

time_until_today_420 = today_420 - now
time_until_today_1620 = today_1620 - now

# print(time_until_today_420)
# print(time_until_today_1620)

if time_until_today_420 >= zero_td or time_until_today_1620 >= zero_td:
    # if either 4:20 or 16:20 is later today
    if time_until_today_1620 < twelve_td:
        # if 16:20 will occur sooner than 12hrs
        time_until_next_420 = time_until_today_1620

    else:
        time_until_next_420 = time_until_today_420

else:
    # else, 4:20 and 16:20 today are already gone, compute tomorrow's
    tomorrow_420 = today_420 + datetime.timedelta(days=1)
    time_until_next_420 = tomorrow_420 - now

# convert timedelta format to seconds for supybot formatter.
time_until_next_420_seconds = time_until_next_420.total_seconds()

# print('Time until next 4:20 : ' + str(time_until_next_420) + f' for {timezone}')

print(format('%T until next 4:20 for %s', time_until_next_420_seconds, timezone_code))
