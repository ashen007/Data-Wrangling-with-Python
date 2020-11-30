class file_handling:
    def __init__(self, path):
        self.__input_file = path

    def read_from(self):
        file = open(self.__input_file, 'r')
        data = file.read()
        file.close()

        return data

    def organize_data(self):
        data = self.read_from()
        rows = data.split('\n')
        header = rows[0]
        rows.pop(0)
        rows.pop()

        for i in range(len(rows)):
            temp = list(rows[i])
            del temp[4]
            temp = ''.join(temp)
            rows[i] = temp.split(',')

        for row in rows:
            temp = list(row[0])
            del temp[0], temp[-1]
            temp = ''.join(temp)
            row[0] = int(temp)
            row[1] = int(row[1])
            row[5] = int(row[5])
            row[8] = float(row[8])

        print(len(data), type(data), len(rows), type(rows))
        for i in range(1, 11):
            print(rows[i])


dataset = file_handling('D:\\data visualition\\sample datasets\\Air_Quality.csv')
dataset.organize_data()
