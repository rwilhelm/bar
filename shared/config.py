from pathlib import Path

import yaml

config_file = Path(__file__).resolve().parent.parent / "config.yaml"
config = yaml.safe_load(open(config_file))

def get_colors(group):
    if group:
        return config["colors"][group]
    return config["colors"]


def get_settings(block_name, setting_name=None):
    try:
        settings = config["blocks"][block_name]["settings"]
    except KeyError:
        return None
    return settings[setting_name] if setting_name else settings


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
