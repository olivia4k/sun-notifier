import asyncio

from sun_notifier.weather import get_weather
from sun_notifier.weather import is_sunny_forcast

from sun_notifier import settings


async def main():
    settings.init()

    for location_name in settings.config['locations']:
        location_weather = await get_weather(location_name)
        is_sunny = is_sunny_forcast(location_weather)
        if is_sunny:
            print("Its a sunny forcast!")
        else:
            print("Not too sunny..")
  
  
if __name__ == '__main__':
    asyncio.run(main())
