import os

class FindPerson:
    def __init__(self):
        self.name = None
        # [year, month, day]
        self.birth = [None, None, None]
        # man, woman
        self.gender = None

    def show_identity(self):
        print('=====IDENTITY=====')
        print(f'Name : {self.name}')
        print(f'birth : {self.birth[0]}/{self.birth[1]}/{self.birth[2]}')
        print(f'gender : {self.gender}')

    def get_identity(self):
        os.system('cls')

        self.name = str(input('Input Person Name(Essential) : '))
        os.system('cls')

        while True:
            try:
                self.birth = str(input('Input Birth(ex. 2007 2 8) : ')).split(' ')
                for i, b in enumerate(self.birth):
                    self.birth[i] = int(b)

                break
            except []:
                print('[!]Please Follow The Format')
        os.system('cls')

        while True:
            try:
                self.gender = str(input('Input gender(ex. man or woman) : '))

                if self.gender != 'man' and self.gender != 'woman':
                    continue

                break
            except []:
                print('[!]Please Follow The Format')
        os.system('cls')

    def facebook_search(self):
        search_url = f'ko-kr.facebook.com/public/{self.name}'


a = FindPerson()

a.get_identity()
a.show_identity()