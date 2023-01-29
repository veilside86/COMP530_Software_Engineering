import secrets
import urllib3
import json
import base64


def save_data(data, filename='wufoo.text'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        file.close()


def get_data():
    subdomain = 'veilside'
    key = secrets.key
    url = f'https://{subdomain}.wufoo.com/api/v3/'
    password = secrets.password

    http = urllib3.PoolManager()
    r = http.request(
        'GET',
        url + 'forms/cubes-project-proposal-submission/entries.json?sort=EntryId&sortDirection=DESC',
        headers={'Authorization': 'Basic ' + base64.b64encode(f'{key}:{password}'.encode()).decode()}
    )
    data = json.loads(r.data.decode('utf-8'))
    # print(json.dumps(data, indent=4, sort_keys=True))

    return data


if __name__ == '__main__':
    all_data = get_data()
    save_data(all_data)
