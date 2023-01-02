import flet as ft
from flet import View
from flet import UserControl, Page
import os, importlib.util
from pages.login import __view__ as v1
from pages.home import __view__ as v2
import pyrebase

_moduleList = {}
for root, dirs, __ in os.walk(r"./"):
    for dir in dirs:
        if dir == "pages":
            for filename in os.listdir(dir):
                _file = os.path.join(dir, filename)
                if os.path.isfile(_file):
                    filename = filename.strip(".py")
                    _moduleList[
                        f"/{filename}"
                    ] = importlib.util.spec_from_file_location(filename)

for i in _moduleList:
    print(i)


firebaseConfig = {
    "apiKey": "AIzaSyAyNHQdLavkZrorZr-OdQ0Px3DKtvnrwmc",
    "authDomain": "healthbudd-initial.firebaseapp.com",
    "databaseURL": "https://healthbudd-initial-default-rtdb.firebaseio.com",
    "projectId": "healthbudd-initial",
    "storageBucket": "healthbudd-initial.appspot.com",
    "messagingSenderId": "198554498567",
    "appId": "1:198554498567:web:4decf44af73786ebb29ca2",
    "measurementId": "G-W2SL219Z50",
}
firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


def main(page: Page):
    page.title = "Hostels"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 1280
    page.window_height = 960
    page.window_min_width = 1280
    page.window_min_height = 960
    page.update()

    login = v1()
    home = v2()

    login.horizontal_alignment = "center"
    login.vertical_alignment = "center"
    home.horizontal_alignment = "center"
    home.vertical_alignment = "center"

    def troca_paginas(route):
        page.views.clear()
        if page.route == "/login":
            page.views.append(login)
        if page.route == "/home":
            page.views.append(home)
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = troca_paginas
    page.on_view_pop = view_pop
    page.go(page.route)

    page.views.append(home)
    page.views.append(login)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
