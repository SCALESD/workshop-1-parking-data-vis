import json


def get_config():
    # Read the config.json file
    config = []
    with open('config.json', 'r') as f:
        config = json.load(f)

    assert 'GoogleMapsAPIKey' in config and len(config['GoogleMapsAPIKey']) > 0, (
           "Add your own Google Maps API Key to config.json")

    return config
