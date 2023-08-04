class Message_history:

    def __init__(self):
        self.history= dict()

    def add_key(self, employee_id):
        if self.history.get(employee_id) is not None:
            ...
        else:
            self.history[employee_id] = list()

    def print_dict(self):
        print(self.history)

    def instring_print(self):
            for key in self.history.keys():
                print(str("{"f"{key}: ") + str(self.dict[key]) + "}\n")

    def instring_save(self, file):
        with open(file, "a") as file:
            for key in self.history.keys():
                file.write(str("{"f"{key}: ") + str(self.history[key]) + "}\n")

    def instring_write(self, file):
        with open(file, "w") as file:
            for key in self.history.keys():
                file.write(str("{"f"{key}: ") + str(self.history[key]) + "}\n")


class Application:

    def __init__(self):
        self.dict = dict()

    def add_key(self, employee_id):
        if self.dict.get(employee_id) is not None:
            ...
        else:
            self.dict[employee_id] = {
                "Name": "",
                "Stage": "0",
                "City": "",
                "Employment_type": "",
                "Age": "",
                "Transport": "",
                "Referral": ""
            }

    def print_dict(self):
        print(self.dict)

    def instring_print(self):
            for key in self.dict.keys():
                print(str("{"f"{key}: ") + str(self.dict[key]) + "}\n")

    def instring_save(self, file):
        with open(file, "a") as file:
            for key in self.dict.keys():
                file.write(str("{"f"{key}: ") + str(self.dict[key]) + "}\n")

    def instring_write(self, file):
        with open(file, "w") as file:
            for key in self.dict.keys():
                file.write(str("{"f"{key}: ") + str(self.dict[key]) + "}\n")