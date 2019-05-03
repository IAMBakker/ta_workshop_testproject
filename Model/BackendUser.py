import json


class User:
    def __init__(self, username, password, role=None, id=None, active=None):
        self.userName = username
        self.passWord = password
        if id is not None:
            self.id = id

        if role is not None:
            self.role = role

        if active is not None:
            self.active = active

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)