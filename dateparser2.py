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
        # If parsing fails, return None
        return None

def process_json_file(input_file, output_file, baddate_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_data = []
    baddate_data = []

    for item in data:
        release_date = item.get('release_date', 'unknown')
        parsed_date = convert_release_date(release_date)
        
        if parsed_date is not None:
            item['release_date'] = parsed_date
            updated_data.append(item)
        else:
            baddate_data.append(item)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, indent=2, cls=DateTimeEncoder)

    with open(baddate_file, 'w', encoding='utf-8') as f:
        json.dump(baddate_data, f, indent=2)
        
if __name__ == "__main__":
    input_file = "SteamScrap/GAMES2.json"
    output_file = "SteamScrap/GAMES4.json"
    baddate_file = "baddate.json"
    process_json_file(input_file, output_file, baddate_file)

