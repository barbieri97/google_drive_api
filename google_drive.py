import argparse

from actions.upload import GoogleDriveUpload
from actions.download import GoogleDriveDownload
from actions.list import GoogleDriveList
from authentication.authenticate import service

parser = argparse.ArgumentParser()
parser.add_argument('command', help='comando a ser executado pela programa')
parser.add_argument('-f', '--file', help="""arquivo para fazer o upload google
                    drive""", required=True)
parser.add_argument('--folder', help="""nome da pasta que deseja fazer o upload
                    do arquivo""")
args = parser.parse_args()

if __name__ == '__main__':
    if args.command == 'upload':
        client = GoogleDriveUpload(service=service)
        if args.folder:
            client.upload_to_folder(args.file, args.folder)
        else:
            client.upload(args.file)
    
    if args.command == 'download':
        client = GoogleDriveDownload(service=service)
        client.download(args.file)
    
    if args.command == 'ls':
        client = GoogleDriveList(service=service)
        client.list(args.file)