from .content_id import GoogleDriveContentId
from googleapiclient.errors import HttpError

class GoogleDriveList(GoogleDriveContentId):
    
    def list(self, folder_name):
        folder_id = self.folder_id(folder_name)
        if not folder_id or type(folder_id) != str:
            return
        files = []
        page_token = None
        try:
            while True:
                response = self.service.files().list(
                    q=f"'{folder_id}' in parents and trashed=false",
                    fields='nextPageToken, files(name, mimeType)',
                    pageToken=page_token
                    ).execute()
                files.extend(response.get('files', []))
                page_token = response.get('nextPageToken')
                if not page_token:
                    break

        except HttpError as error:
            print(f'Am error occurred: {error}')
            return
        
        for file in files:
            print(f"{file.get('name')} - {file.get('mimeType')}")
        return files