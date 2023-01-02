import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, colors
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
db = firebase.database()


def __view__():
    return View(
        "/home",
        [
            ft.Text("Home", size=50, weight=ft.FontWeight.BOLD),
        ],
    )
