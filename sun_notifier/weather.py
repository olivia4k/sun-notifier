import python_weather
from datetime import time

from sun_notifier import settings


async def get_weather(location_name: str):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast for a location_name
        weather = await client.get(location_name)
        return weather

def get_avg_stats(forcasts):
    count = 0
    total_cloud_cover = 0
    total_chances_of_sunshine = 0
    for forcast in forcasts:
        # todays, tommorow and after-tommorow forcasts
        for hourly in forcast.hourly:
            if hourly.time in [time(0,0,0), time(3,0,0)]:
                # exclude night forcasts
                continue 
            count += 1
            total_cloud_cover += hourly.cloud_cover
            total_chances_of_sunshine += hourly.chances_of_sunshine
    avg_cloud_cover = total_cloud_cover//count
    avg_chances_of_sunshine = total_chances_of_sunshine//count
    return avg_cloud_cover, avg_chances_of_sunshine

def is_sunny_forcast(weather):
    forcasts = list(weather.forecasts)
    avg_cloud_cover, avg_sunshine = get_avg_stats(forcasts)
    is_not_cloudy = avg_cloud_cover < settings.config['cloud_cover_threshold']
    is_sunshine = avg_sunshine > settings.config['sunshine_threshold']
    return is_not_cloudy and is_sunshine