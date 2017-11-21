

class TransData(object):
    _instance = None
    file = None
    str_list = []
    val_list = []

    def load(self):
        self.file = open("data.txt", "r+")
        content = self.file.readlines()
        self.str_list.clear()
        self.val_list.clear()
        for line in content:
            self.str_list.append(line.split()[0])
            self.val_list.append(int(line.split()[1]))
        self.file.close()

    def save(self):
        self.file = open("data.txt", "w")
        for i in range(0, len(self.str_list)):
            self.file.write(self.str_list[i] + " " + str(self.val_list[i]) + "\n")
        self.file.close()

    def add(self, string, value):
        found = False
        for i in range(0, len(self.str_list)):
            if self.str_list[i] == string:
                self.val_list[i] = value
                found = True
        if not found:
            self.str_list.append(string)
            self.val_list.append(value)
        self.save()

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
            cls.load(cls)
        return cls._instance
