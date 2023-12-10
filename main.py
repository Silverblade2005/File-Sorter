import os
import shutil

file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico', '.jfif', '.pjpeg', '.pjp'],
    'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.3gp', '.ogg', '.m4v'],
    'audios': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a', '.amr', '.aiff', '.mid', '.midi'],
    'documents': ['.doc', '.docx', '.pdf', '.ppt', '.pptx', '.xls', '.xlsx', '.txt', '.rtf', '.odt', '.ods', '.odp', '.csv']
}

script_directory = os.path.dirname(os.path.realpath(__file__))

def start_sorting():
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

def edit_extentions(type_file, new_extentions):
    for ext in new_extentions:
        file_types[type_file].append(ext)
    print(f"{new_extentions} will now be classified as {type_file}")

extentions = []
def add_prompt():
    r_extentions = []
    extention = input("Type your extention (example: '.png') here:\n ")
    extentions.append(extention)
    prompt = int(input("Want to add another \n 1. Yes \n 2. No\n"))
    if prompt == 1:
        add_prompt()
    elif prompt == 2:
        pass
    else:
        print("Invalid Prompt, Try again!")
        add_prompt()
    print(extentions)
    return extentions

def start_menu():
    menu_text = """
        Welcome to the file sorter, enter a a number representing what you want to do:\n
        1. Edit the what files will be classified as images
        2. Edit the what files will be classified as audios
        3. Edit the what files will be classified as videos
        4. Edit the what files will be classified as documents
        5. Start Sorting
        6. Terminate Program\n
    """
    user_input = input(menu_text)
    main(int(user_input))
    

def main(user_input):
    if user_input < 5:
        if user_input == 1:
            type_file = "images"
            exts = add_prompt()
            print(exts)
            edit_extentions(type_file, exts)
        elif user_input == 2:
            type_file = "audios"
            exts = add_prompt()
            edit_extentions(type_file, exts)
        elif user_input == 3:
            type_file = "videos"
            exts = add_prompt()
            edit_extentions(type_file, exts)
        elif user_input == 4:
            type_file = "documents"
            exts = add_prompt()
            edit_extentions(type_file, exts)
        else:
            print("Your prompt was invalid, try again.")
        start_menu()
    elif user_input == 5:
        start_sorting()
        print("Sorting Complete.")
        start_menu()
    elif user_input == 6:
        print("Thank you for using this program. Goodbye!")
    else:
        print("Your prompt was invalid, try again.")

start_menu()