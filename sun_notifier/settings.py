import yaml

def init():
    global config
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)