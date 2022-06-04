class MyList:
    def __init__(self, default_type):
        if default_type is float or default_type is int:
            self.default_type = default_type
        else:
            raise Exception("Notimplemented")

