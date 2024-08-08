import requests
import json


class Parser:
    url = 'https://opendata.mkrf.ru/v2/cinema/$?l=300'  # 300 позиций

    """ https://opendata.mkrf.ru/item/api"""

    @classmethod
    def get_json(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Cookie': 'apisid=VjVXbBDTwCoNGSGi1%2FmWyZRK59N5WzkUYlmE%2FfDbi%2FUal5egjRJVqwv7z7V5HRfV86uRkO9w1kcpjJshoq7n8xcKXZ3PXTutZcTVuTM4LqSQixs7pW1hAMKg%2BPJvKY%2FG8GhqmAUk%2Bjw%2BH6W1ZIM1nnqEr839yzsM3uZp75lhPi4%3D'

        }
        results = requests.get(self.url, headers=headers)
        print(results.status_code)
        print(f'[INFO] Сохраняю json')
        with open('cinema.json', 'w', encoding='utf-8') as file:
            json.dump(results.json(), file, indent=4, ensure_ascii=False)
        print(f'[INFO] Сохранил json')

    def run(self):
        self.get_json()


if __name__ == '__main__':
    Parser().run()
