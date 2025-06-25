import requests
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import rcParams

# 日本語フォント設定
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro']

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
        
        # グラフを作成
        create_monthly_chart(monthly_events)
    else:
        print("イベントが見つかりませんでした。")

def create_monthly_chart(monthly_events):
    """月毎のイベント数を折れ線グラフで表示"""
    # データを準備
    months = []
    counts = []
    
    for month in sorted(monthly_events.keys()):
        year, month_num = month.split('-')
        # datetimeオブジェクトを作成（グラフのX軸用）
        dt = datetime(int(year), int(month_num), 1)
        months.append(dt)
        counts.append(monthly_events[month])
    
    # グラフを作成
    plt.figure(figsize=(12, 6))
    plt.plot(months, counts, marker='o', linewidth=3, markersize=8, color='#2E86AB', markerfacecolor='#A23B72', markeredgecolor='#2E86AB', markeredgewidth=2)
    
    # グラフの設定
    plt.title('月毎のイベント数', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('月', fontsize=12)
    plt.ylabel('イベント数', fontsize=12)
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # X軸の日付フォーマット
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y年%m月'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.xticks(rotation=45)
    
    # データポイントの上に数値を表示
    for i, (month, count) in enumerate(zip(months, counts)):
        plt.text(month, count + 0.1, str(count), ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    # 背景色を設定
    plt.gca().set_facecolor('#f8f9fa')
    plt.gcf().set_facecolor('white')
    
    plt.tight_layout()
    plt.savefig('monthly_events.png')
    plt.close()

if __name__ == '__main__':
    api_key = 'YOUR_API_KEY'
    calendar_id = 'en.usa#holiday@group.v.calendar.google.com'  # TODO: 取得したいカレンダーIDにする

    url = f'https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events?key={api_key}'
    events = fetch_all_events(url)

    print(f'総イベント数: {len(events)}')
    monthly_events(events)
