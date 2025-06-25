import requests

api_key = 'YOUR_API_KEY'
calendar_id = 'en.usa#holiday@group.v.calendar.google.com'  # 公開カレンダーのID（例：アメリカの祝日）

url = f'https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events?key={api_key}'

events = []
page_token = None

while True:
    params = {'pageToken': page_token} if page_token else {}
    response = requests.get(url, params=params)
    data = response.json()
    events.extend(data.get('items', []))
    page_token = data.get('nextPageToken')
    if not page_token:
        break

print(f'イベント数: {len(events)}')
