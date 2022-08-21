import requests
from pprint import pprint
from datetime import datetime, timezone


def get_questions_on_stack_stackoverflow(days_shift, tag):
    to_date = int(datetime.timestamp(datetime.today()))
    from_date = int(datetime.timestamp(datetime(datetime.today().year,
                                                datetime.today().month, datetime.today().day - days_shift,
                                                tzinfo=timezone.utc)))
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': from_date,
              'todate': to_date,
              'order': 'desc',
              'sort': 'creation',
              'tagged': tag,
              'site': 'stackoverflow'}
    response = requests.get(url, params=params)
    print(f'Статус выполнения запроса: {response.status_code}')
    pprint(response.json())


if __name__ == '__main__':

    get_questions_on_stack_stackoverflow(2, 'Python')
