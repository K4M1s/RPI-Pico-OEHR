import storage


class Config:

    def __init__(self):
        self.filename = '/config.txt'
        self.min = 0
        self.max = 100
        self.range_min = 0
        self.range_max = 65535
        self.read()

    def read(self):
        try:
            file = open(self.filename, 'r')
            lines = file.readlines()
            if len(lines) == 4:
                self.min = int(lines[0].strip())
                self.max = int(lines[1].strip())
                self.range_min = int(lines[2].strip())
                self.range_max = int(lines[3].strip())
            file.close()
        except OSError:
            print('Failed to read config.')

    def write(self):
        try:
            file = open(self.filename, 'w')
            file.write(str(self.min) + '\n')
            file.write(str(self.max) + '\n')
            file.write(str(self.range_min) + '\n')
            file.write(str(self.range_max) + '\n')
            file.close()
        except OSError:
            print('Failed to write config.')
