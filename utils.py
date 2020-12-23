import os
import tarfile


def unpack_archived_data():
    archive_path = os.path.abspath(os.path.join('data', 'edf.tar.gz'))
    if 'edf' not in os.listdir(os.path.dirname(archive_path)):
        with tarfile.open(archive_path) as file:
            file.extractall(path=os.path.dirname(archive_path))
        print('Unpacking finished')
