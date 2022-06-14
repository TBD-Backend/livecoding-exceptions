from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")


class BaseConfigError(Exception):
    pass



class BaseConfig:
    OPEN_WEATHER_MAP_API_KEY = config["api"]["open_weather_map_key"]
    LATITUDE = config.getfloat("general", "latitude")
    LONGITUDE = config.getfloat("general", "longitude")
    CACHE_EXPIRES_AFTER = config.getint("cache", "cache_expires_after") or 0
    DEFAULT_LANGUAGE = "en"
    LANGUAGE = (
        DEFAULT_LANGUAGE
        if config["general"]["language"] is None
        else config["general"]["language"]
    )
    MEMCACHED_SERVER = config["cache"]["memcached"]



if BaseConfig.OPEN_WEATHER_MAP_API_KEY is None:
    raise BaseConfigError("OPEN_WEATHER_MAP_API_KEY is missing")

if BaseConfig.DEFAULT_LANGUAGE is None:
    raise BaseConfigError("Missing default language")