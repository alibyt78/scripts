import shutil
import os

source = 'test_folder'
destination = 'backup_folder'

if not os.path.exists(source):
    os.makedirs(source)
    with open(os.path.join(source, 'sample.txt'), 'w') as f:
        f.write('Sample file content')

shutil.copytree(source, destination, dirs_exist_ok=True)
print('Backup completed successfully!')
