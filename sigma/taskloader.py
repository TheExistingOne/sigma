import glob
import os
import yaml


def parse_tasks():
    tasks = []
    os.chdir("tasks")
    # Iterate over all files in /tasks with the extension .yaml
    # parse them, and add them to the array
    for file in glob.glob("*.yaml"):
        tasks.append(parse_yaml_to_dictionary(file))
    return tasks


def parse_yaml_to_dictionary (config):
    # Template dictionary to load data in to
    parsed_config = {
        "name": "",
        "notify": False,
        "notification-body": "",
        "day": 00,
        "month": 00,
        "year": 00,
        "hour": 00,
        "minute": 00
    }
    with open(config, 'r') as stream:
        try:
            # Load simple values from config
            raw_config = yaml.safe_load(stream)
            parsed_config["name"] = raw_config.get("name")
            parsed_config["notify"] = raw_config.get("notify")
            parsed_config["notification-body"] = raw_config.get("notification-body")
            
            #Load and parse timestamp into it's components and load them
            timestamp_separated = raw_config.get("notify-timestamp").split("-")
            parsed_config["day"] = int(timestamp_separated[0])
            parsed_config["month"] = int(timestamp_separated[1])
            parsed_config["year"] = int(timestamp_separated[2])
            parsed_config["hour"] = int(timestamp_separated[3])
            parsed_config["minute"] = int(timestamp_separated[4])

        except yaml.YAMLError as e:
            print(e)

    return parsed_config
