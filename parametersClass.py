import sys


class Parameters:
    config = {
        "marginTopText" : 100,
        "marginTopImg" : 100,
        "fontSize" : 150,
        "logoScale" : 0.8,
        "font" : "fonts/font.ttf",
        "shape": "shape.png",
        "logo": "logo.png",
        "countStart": 1,
        "countStop": 10
    }

    def __init__(self):
        try:
            file = open("config.txt", "r")
            lines = file.readlines()
            for line in lines:
                if line.split("-")[0] in self.config:
                    self.config[line.split("-")[0]] = line.split("-")[1]
        except:
            self.create_config_file()
            input("Error with opening file, new one has been created if not exist")
            sys.exit(0)

    def print_config(self):
        print(self.config)

    def create_config_file(self):
        content = ""
        for key in self.config:
            content += key + "-" + str(self.config[key]) + "\n"
        with open('config.txt', 'w') as f:
            f.write(content)

