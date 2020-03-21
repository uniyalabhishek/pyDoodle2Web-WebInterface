from bs4 import BeautifulSoup
import os

class Navbar:
    def __init__(self):
        self.name = 'navbar'
        self.isParentLike = False

        with open(os.path.join(os.getcwd(), 'components', 'navbar', 'template.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
        self.template = soup
