import os
import shutil

file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico', '.jfif', '.pjpeg', '.pjp'],
    'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.3gp', '.ogg', '.m4v'],
    'audios': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a', '.amr', '.aiff', '.mid', '.midi'],
    'documents': ['.doc', '.docx', '.pdf', '.ppt', '.pptx', '.xls', '.xlsx', '.txt', '.rtf', '.odt', '.ods', '.odp', '.csv']
}

script_directory = os.path.dirname(os.path.realpath(__file__))
print(script_directory)

for category in file_types:
    folder_path = os.path.join(script_directory, category)
    os.makedirs(folder_path, exist_ok=True)

for file_name in os.listdir(script_directory):
    file_path = os.path.join(script_directory, file_name)

    if os.path.isfile(file_path):
        file_type = None
        for category, extensions in file_types.items():
            if any(file_name.lower().endswith(ext) for ext in extensions):
                file_type = category
                break
        
        if file_type:
            destination_folder = os.path.join(script_directory, file_type)
            destination_path = os.path.join(destination_folder, file_name)
            shutil.move(file_name, destination_path)
            print(f"File '{file_name}' has been moved to '{destination_path}.' ")
