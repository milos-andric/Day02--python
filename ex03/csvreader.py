from pprint import pprint


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exception has been handled")
        self.file.close()
        return True

    def getdata(self):
        got = self.file.read()
        return(got)

    def getheader(self):
        print('FFFFF')
        stred = self.file.getdata()
        print('FFFFF')
        stred = stred.split('\n')
        print('FFFFF')
        stred = str(stred[0])
        print('FFFFF')


if __name__ == "__main__":
    with CsvReader('file.csv') as file:
        print("ok")
        data = file.getdata()
        print(data)
        header = file.getheader()
