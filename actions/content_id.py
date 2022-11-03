from googleapiclient.errors import HttpError


class GoogleDriveContentId:
    def __init__(self, service) -> None:
        self.service = service

    def folder_id(self, folder_name):
        try:
            response = self.service.files().list(
                q=f"name='{folder_name}' and"
                "mimeType='application/vnd.google-apps.folder' and"
                "trashed=false",
                fields='files(id)'
                                                ).execute()
            files = response.get('files')
            if not files:
                print(
                    'A pasta que procura não existe ou há mais de uma pasta'
                    'com esse nome'
                    )
                return
            if len(files) > 1:
                print(
                    'Há mais de uma pasta com o nome que digitou\n\nSegue o'
                    'link para cada uma delas:\n'
                    )
                for i in files:
                    print(
                         f"""https://drive.google.com/drive/folders/{
                            i.get("id")
                            }"""
                        )
                return
            return files[0].get('id')
        except HttpError as error:
            print(f'An error ocurred: {error}')
            return

    def file_id(self, file_name):
        try:
            response = self.service.files().list(
                q=f"name='{file_name}' and not"
                "mimeType='application/vnd.google-apps.folder' and"
                "trashed=false",
                fields='files(id, parents)'
                ).execute()
            files = response.get('files')
            if not files:
                print(
                    f'O arquivo {file_name} não existe ou há mais de uma pasta'
                    'com esse nome')
                return
            if len(files) > 1:
                print(
                    f'Há mais de um arquivo com o nome {file_name}:\n\nSegue o'
                    'link para a pasta desses arquivos:\n')
                for i in files:
                    print(f"""https://drive.google.com/drive/folders/{
                        i.get("parents")[0]}""")
                return
            return files[0].get('id')
        except HttpError as error:
            print(f'An error ocurred: {error}')
            return
