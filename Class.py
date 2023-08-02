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

    def instring(self):
        return str(self.history)


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

    def instring(self):
        return str(self.dict)