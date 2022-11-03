from mimetypes import guess_type
from os import path

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from .content_id import GoogleDriveContentId

class GoogleDriveUpload(GoogleDriveContentId):

    def upload(self, file):

        try:
            file_metadata = {
                'name': path.basename(file),
            }
            media = MediaFileUpload(file,
                                    mimetype=guess_type(file)[0], resumable=True)
            # pylint: disable=maybe-no-member
            file = self.service.files().create(body=file_metadata, media_body=media,
                                          fields='id').execute()
            print(F'File with ID: "{file.get("id")}" has added to My Drive')
    
        except HttpError as error:
            print(F'An error occurred: {error}')
            file = None
    
        return file.get('id')

        

    def upload_to_folder(self, file, folder_name):

        folder_id = self.folder_id(folder_name)
        if not folder_id:
            return 
        try:
            file_metadata = {
                'name': path.basename(file),
                'parents': [folder_id]
            }
            media = MediaFileUpload(file,
                                    mimetype=guess_type(file)[0], resumable=True)
            # pylint: disable=maybe-no-member
            file = self.service.files().create(body=file_metadata, media_body=media,
                                          fields='id').execute()
            print(F'File with ID: "{file.get("id")}" has added to the folder with '
                  F'ID "{folder_id}".')
    
        except HttpError as error:
            print(F'An error occurred: {error}')
            file = None
    
        return file.get('id')