import requests
from datetime import datetime
from collections import defaultdict



def fetch_all_events(url):

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
    
    return events

def monthly_events(events):
    # 毎月のイベント数を集計
    monthly_events = defaultdict(int)

    for event in events:
        # イベントの開始日時を取得
        start_date = event.get('start', {}).get('dateTime') or event.get('start', {}).get('date')

        if start_date:
            try:
                # 日時文字列をパース
                if 'T' in start_date:  # dateTime形式
                    dt = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
                else:  # date形式
                    dt = datetime.fromisoformat(start_date)

                # 年月をキーとして使用 (YYYY-MM形式)
                month_key = dt.strftime('%Y-%m')
                monthly_events[month_key] += 1

            except ValueError as e:
                print(f"日付のパースエラー: {start_date}, エラー: {e}")

    # 結果を表示
    print("\n=== 毎月のイベント数 ===")
    if monthly_events:
        # 月順にソートして表示
        for month in sorted(monthly_events.keys()):
            year, month_num = month.split('-')
            month_name = datetime(int(year), int(month_num), 1).strftime('%Y年%m月')
            print(f"{month_name}: {monthly_events[month]}件")
    else:
        print("イベントが見つかりませんでした。")

if __name__ == '__main__':
    api_key = 'YOUR_API_KEY'
    calendar_id = 'en.usa#holiday@group.v.calendar.google.com'  # TODO: 取得したいカレンダーIDにする

    url = f'https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events?key={api_key}'
    events = fetch_all_events(url)

    print(f'総イベント数: {len(events)}')
    monthly_events(events)
