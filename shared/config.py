#!/usr/bin/env python


import yaml

def config():
    return yaml.safe_load(open("config.yaml"))


if __name__ == "__main__":
    config()
