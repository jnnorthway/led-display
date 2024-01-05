import os
import yaml
import pathlib


def load_config():
    calm_directory = pathlib.Path(__file__).parent.resolve()
    config_path = os.path.join(calm_directory, "config.yaml")
    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)
    if config:
        return config
    print(f"Failed to load config from: {config_path}")
    exit(1)
