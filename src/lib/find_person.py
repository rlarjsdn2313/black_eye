import os
import time

from selenium import webdriver


class FindPerson:
    def __init__(self, web_driver_path: str):
        self.name = None
        # [year, month, day]
        self.birth = [None, None, None]
        # man, woman
        self.gender = None

        self.web_driver_path = web_driver_path

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(executable_path=self.web_driver_path, options=options)

        self.scroll_second = 3

        self.facebook_basic_url = 'https://ko-kr.facebook.com/public/'

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
                os.system('cls')
                print('[!]Please Follow The Format')
        os.system('cls')

        while True:
            try:
                self.gender = str(input('Input gender(ex. man or woman) : '))

                if self.gender != 'man' and self.gender != 'woman':
                    os.system('cls')
                    print('[!]Please Follow The Format')
                    continue

                break
            except []:
                os.system('cls')
                print('[!]Please Follow The Format')

        os.system('cls')

    def scroll_to_bottom(self):
        last_height = self.driver.execute_script('return document.body.scrollHeight')

        # scroll to bottom
        while True:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(self.scroll_second)
            new_height = self.driver.execute_script('return document.body.scrollHeight')

            if new_height == last_height:
                break

            last_height = new_height

        # go to top
        self.driver.execute_script('window.scrollTo(0, 0);')

    def facebook_search(self):
        # set url to search
        search_url = self.facebook_basic_url + self.name

        # go to search url
        self.driver.get(search_url)

        time.sleep(3)

        print('Loading people...')

        # get all data
        self.scroll_to_bottom()


a = FindPerson(web_driver_path=f'{os.getcwd()}\\chromedriver.exe')

a.get_identity()
a.show_identity()
a.facebook_search()
