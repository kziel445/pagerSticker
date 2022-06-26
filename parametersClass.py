class Parameters:
    config = {
        "marginTopText" : 100,
        "marginTopImg" : 100,
        "fontSize" : 150,
        "logoScale" : 0.8,
        "font" : " ",
        "shape": " ",
        "logo": " ",
        "countStart":"",
        "countStop": ""
    }

    def __init__(self):
        try:
            file = open("config", "r")
            lines = file.readlines()
            for line in lines:
                if line.split("-")[0] in self.config:
                    self.config[line.split("-")[0]] = line.split("-")[1]
        except:
            print("Error with opening file")

    def print_config(self):
        print(self.config)
