class MyClass(self):
    n_objects = 0

    def __new__(cls):
        if cls.n_objects < 5:
            cls.n_objects += 1
            return object.__new__(cls)
        return None

    def __str__(self):
        print("")
        return "An object of MyClass"
