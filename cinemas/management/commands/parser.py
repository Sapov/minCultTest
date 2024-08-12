import requests
import json


class Parser:
    url = 'https://opendata.mkrf.ru/v2/cinema/$?l=300'  # 300 позиций

    """ https://opendata.mkrf.ru/item/api"""

    @classmethod
    def get_json(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/127.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/'
                      'webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Cookie': 'ck_session=eyJjYXB0Y2hhIjoiNDQ3NDY0In0=; ck_session.sig=MG4PIaV0z2emuBbG4dMpX1sSzuY; apisid=Dl2P%2FliLCCvhQwOkQT2GNb8ZNZD2imYKvlW%2Fm3q5%2FpLPX9WA%2F6PgeiuNsimyxVMGQLoORlX3x3VqXoP6HKGY1u8VWRqEevjnNArBE8f2WK4pmNF7YuLAb%2B31Fj6JJGRP%2BiLIgK6gCcqTr2TDQ%2FFIqO7AUp812TtRxJgQ7XCjzvo%3D'
        }
        results = requests.get(self.url, headers=headers)
        print(f'[INFO] {results.status_code}')
        print(f'[INFO] Сохраняю json')
        with open('cinema.json', 'w', encoding='utf-8') as file:
            json.dump(results.json(), file, indent=4, ensure_ascii=False)
        print(f'[INFO] Сохранил json')

    def run(self):
        self.get_json()


if __name__ == '__main__':
    Parser().run()
