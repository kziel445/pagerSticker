import sys


class Parameters:
    config = {
        "marginTopText" : 100,
        "marginTopImg" : 100,
        "fontSize" : 150,
        "logoScale" : 0.8,
        "font" : "",
        "shape": "",
        "logo": "",
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
            input("Error with opening file")
            sys.exit(0)

    def print_config(self):
        print(self.config)
