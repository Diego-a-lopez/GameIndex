import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def convert_release_date(date_str):
    try:
        # Try to parse the date using the specified format
        date_object = datetime.strptime(date_str, "%d %b, %Y")
        return date_object
    except ValueError:
        try:
            # Try another format with the day set to the first day of the month
            date_object = datetime.strptime(date_str, "%b %Y")
            date_object = date_object.replace(day=1)
            return date_object
        except ValueError:
            # If parsing fails, return 'unknown'
            return 'unknown'

def process_json_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        release_date = item.get('release_date', 'unknown')
        item['release_date'] = convert_release_date(release_date)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, cls=DateTimeEncoder)

if __name__ == "__main__":
    input_file = "SteamScrap/GAMES2.json"
    output_file = "SteamScrap/GAMES3.json"
    process_json_file(input_file, output_file)
