import os

directory = 'batch_files'
os.makedirs(directory, exist_ok=True)

# Create dummy files
for i in range(3):
    with open(os.path.join(directory, f'file_{i}.txt'), 'w') as f:
        f.write('dummy')

# Rename all files with prefix 'renamed_'
for filename in os.listdir(directory):
    os.rename(os.path.join(directory, filename), os.path.join(directory, 'renamed_' + filename))

print('All files renamed successfully!')
