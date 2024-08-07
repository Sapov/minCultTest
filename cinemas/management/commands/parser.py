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
        with open('cinema.json', 'w', encoding='utf-8') as file:
            json.dump(results.json(), file, indent=4, ensure_ascii=False)

    def load_data(self):
        with open('cinema_old.json', 'r', encoding='utf-8') as file:
            d = json.load(file)
            # print(d.keys())
            # print(d['data'])
            # print(len(d['data']))
            for i in d['data']:
                # print(i['data']['general'])
                id = i['data']['general']['id']
                name = i['data']['general']['name']
                description = i['data']['general']['description']
                address = i['data']['general']['address']
                # print(address)
                contacts = i['data']['general'].get('contacts', None)
                if contacts != None:
                    print(contacts)
                    website = contacts.get('website', None)
                    email = contacts.get('email', None)
                    print(email)
                    phones = contacts.get('phones', None)
                    if phones:
                        for j in phones:
                            print(j['value'], j['comment'])

                # website = i['data']['general'].get('contacts', None).get('website', None)

                # if i['data']['general']['contacts']['email']:
                #     email = i['data']['general']['contacts']['email']
                #     print(email)
                # email = None
                # phones = i['data']['general']['contacts']['phones']
                # mapPosition = i['data']['general']['mapPosition']['coordinates']

    def run(self):
        self.get_json()
        # self.load_data()


if __name__ == '__main__':
    Parser().run()
