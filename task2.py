import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, ya_disk_file_path: str, local_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': ya_disk_file_path, 'overwrite': 'True', }
        headers = {'Authorization': f'OAuth {self.token}'}
        upload_path = requests.get(upload_url, params=params, headers=headers)
        href = upload_path.json()['href']
        print(f'Статус выполнения запроса загрузки файла: '
              f'{requests.put(href, data=open(local_file_path, "rb")).status_code}')
        return

    def create_folder(self, folder_name):
        create_folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': folder_name}
        print(f'Статус выполнения запроса создания папки {folder_name}: '
              f'{requests.put(create_folder_url, params=params, headers=headers).status_code}')
        return

    def files_on_disk(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = {'Authorization': f'OAuth {self.token}'}
        pprint(f'Информация о файлах на диске:{requests.get(url, headers=headers).json()}')
        return


if __name__ == '__main__':

    token = 'ТОКЕН АГА'
    my_disk = YaUploader(token)

    # Создадим целевую папку /homework/files для загрузки тестового файла
    my_disk.create_folder('homework_http')
    my_disk.create_folder('homework_http/files')

    # Загрузим тестовый файл из папки test_folder
    my_disk.upload('/homework_http/files/test_file.txt', 'test_folder/test_file.txt')

    # Проверяем, есть ли файлы
    my_disk.files_on_disk()
