import flet as ft
from flet import View
from flet import UserControl, Page

from pages.login import __login__
import pyrebase

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

    index = __login__()
    index.horizontal_alignment = "center"
    index.vertical_alignment = "center"
    page.views.append(index)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
