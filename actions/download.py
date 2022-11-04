import io

from .content_id import GoogleDriveContentId

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload


class GoogleDriveDownload(GoogleDriveContentId):

    def download(self, file_name):
        file_id = self.file_id(file_name)
        if not file_id:
            return
        try:
            response = self.service.files().get_media(fileId=file_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, response)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f'Download: {int(status.progress() * 100)}')

        except HttpError as error:
            print(f"An error occurred: {error}")
            return

        data = file.getvalue()
        with open(f'/home/barbieri97/Downloads/{file_name}', 'wb') as arq:
            arq.write(data)

        print(f"arquivo baixado em /home/barbieri97/Downloads/{file_name}")
        return f'/home/barbieri97/Downloads/{file_name}'
