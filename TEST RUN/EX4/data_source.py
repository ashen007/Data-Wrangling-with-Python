import pandas as pd
from bs4 import BeautifulSoup as bs


class listener_data():

    def __init__(self, path):
        self.__data_points_in_page = []
        self.__profile = path

    def read_page(self):
        page = bs(self.__profile)

        return page


ashen = listener_data('https://www.last.fm/user/ashen077/library')
page = ashen.read_page()
print(len(page))