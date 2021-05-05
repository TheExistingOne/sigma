import yaml


def parse_task(config):
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
            raw_config = yaml.safe_load(stream)
            parsed_config["name"] = raw_config.get("name")
            parsed_config["notify"] = raw_config.get("notify")
            parsed_config["notification-body"] = raw_config.get("notification-body")

            timestamp_separated = raw_config.get("notify-timestamp").split("-")
            parsed_config["day"] = int(timestamp_separated[0])
            parsed_config["month"] = int(timestamp_separated[1])
            parsed_config["year"] = int(timestamp_separated[2])
            parsed_config["hour"] = int(timestamp_separated[3])
            parsed_config["minute"] = int(timestamp_separated[4])

        except yaml.YAMLError as e:
            print(e)

    return parsed_config
