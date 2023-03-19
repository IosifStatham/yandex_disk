import requests

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        headers = {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        return headers

    def get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path,'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        href = data.get('href')
        return href

    def upload(self, file_path, file_name):
        href = self.get_upload_link(file_path=file_path)
        resp = requests.put(href, data=open(file_name, 'rb'))
        if resp.status_code == 201:
            return 'Success'


if __name__ == '__main__':
    token = ""
    file = 'Files/text.txt'
    ya = YaUploader(token)
    response = ya.upload('Test/file1.txt', file)
    print(response)