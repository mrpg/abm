class Learning:
    # general-purpose super-class
    def __init__(self, **kwargs):
        self.parameters = kwargs
        self.history = []

    def __getitem__(self, name):
        return self.parameters[name]

    def __setitem__(self, name, value):
        self.parameters[name] = value

    def choose(self):
        pass

    def update(self, action, reward):
        pass

    def archive(self, **kwargs):
        self.history.append(kwargs)
