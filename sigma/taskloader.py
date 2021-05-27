import glob
import os
import yaml
from sigma.database import add_task, run_query

def load_tasks():
    tasks = []

    for task in run_query("SELECT * FROM tasks ORDER BY time"):
        tasks.append(parse_database_to_dictionary(task))

    # os.chdir("tasks")
    # Iterate over all files in /tasks with the extension .yaml
    # parse them, and add them to the array
    for file in glob.glob("tasks/*.yaml"):
        tasks.append(parse_yaml_to_dictionary(file))
        os.remove(file)

    for task in tasks:
        add_task(task.get("name"), task.get("notification-body"), task.get("timestamp"), task.get("notify"))
    # os.chdir("../")
    return tasks


def parse_database_to_dictionary (entry):
    # Template dictionary to load data in to
    parsed_config = {
        "name": "",
        "notify": False,
        "notification-body": "",
        "timestamp": "00-00-00-00-00",
        "day": 00,
        "month": 00,
        "year": 00,
        "hour": 00,
        "minute": 00
    }

    parsed_config["name"] = entry[0]
    parsed_config["notify"] = entry[3]
    parsed_config["notification-body"] = entry[1]

    parsed_config["timestamp"] = entry[2]

    # Load and parse timestamp into it's components and load them
    timestamp_separated = entry[2].split("-")
    parsed_config["day"] = int(timestamp_separated[0])
    parsed_config["month"] = int(timestamp_separated[1])
    parsed_config["year"] = int(timestamp_separated[2])
    parsed_config["hour"] = int(timestamp_separated[3])
    parsed_config["minute"] = int(timestamp_separated[4])

    return parsed_config

def parse_yaml_to_dictionary (config):
    # Template dictionary to load data in to
    parsed_config = {
        "name": "",
        "notify": False,
        "notification-body": "",
        "timestamp": "00-00-00-00-00",
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

            parsed_config["timestamp"] = raw_config.get("notify-timestamp")

            # Load and parse timestamp into it's components and load them
            timestamp_separated = raw_config.get("notify-timestamp").split("-")
            parsed_config["day"] = int(timestamp_separated[0])
            parsed_config["month"] = int(timestamp_separated[1])
            parsed_config["year"] = int(timestamp_separated[2])
            parsed_config["hour"] = int(timestamp_separated[3])
            parsed_config["minute"] = int(timestamp_separated[4])

        except yaml.YAMLError as e:
            print(e)

    return parsed_config
