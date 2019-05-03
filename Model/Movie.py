import json

class Movie:
    def __init__(self, title, year, imdb,
                 type, image=None, description=None):
        self.title = title
        self.year = year
        self.imdb = imdb
        self.type = type
        if image is not None:
            self.image=image
        if description is not None:
            self.description=description

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
