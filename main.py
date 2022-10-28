import os
from venv import create


class Folder:

    def __init__(self):
        self.default_name = 'WebApp'
        self.default_path = os.getcwd()
        self.default_all = f'{self.default_path}\\{self.default_name}'
        self.files = ['index.html', 'main.js', 'style.css']

    folder_name = input("Select folder name:\n")
    folder_path = input(
        "Select folder path: (blank: current working directory)\n")
    final_path = (f'{folder_path}\\{folder_name}')

    def create_folder(self):
        # if nothing is selected, create defaults
        if (self.folder_path != '') and (self.folder_name != ''):
            try:
                os.mkdir(self.final_path)
                print('Succesfully created directory')
                return (self.final_path)
            except FileExistsError as e:
                print(f'Folder already exists: {e}')


        # created folder with current path
        elif (self.folder_path == '') and (self.folder_name != ''):
            try:
                os.mkdir(f'{self.default_path}\\{self.folder_name}')
                print('Succesfully created directory in current working dir')
                return (f'{self.default_path}\\{self.folder_name}')
            except FileExistsError as e:
                print(f'Folder already exists {e}')

        # create default dir
        else:
            try:
                os.mkdir(f'{self.default_all}')
                print('Succesfully created default directory')
                return (f'{self.default_all}')
            except FileExistsError as e:
                print(f'Folder already exists {e}')


    def create_files(self):
        name_of_path = self.create_folder()
        python_script_path = os.path.dirname(__file__)
        # get file names from list
        for file in self.files:
            # create the files
            with open(f'{name_of_path}\\{file}', 'w') as f:
                # copy a boilerplate html text from boiler.txt when we create the html file
                if file == self.files[0]:
                    with open(f'{python_script_path}\\boiler.txt', 'r') as index_html:
                        for text in index_html:
                            f.write(text)


if __name__ == "__main__":
    f1 = Folder()
    print(f1.create_files())
