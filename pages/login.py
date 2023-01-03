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


email = ft.TextField(
    label="Email",
    # hint_text="Seu email para login",
    border=ft.InputBorder.NONE,
    filled=True,
    width=300,
)
senha = ft.TextField(
    label="Senha",
    # hint_text="Senha senha",
    password=True,
    can_reveal_password=True,
    border=ft.InputBorder.NONE,
    filled=True,
    width=300,
)


def page_goto(e):
    e.page.go("/home")


def create_account(e):
    page_goto(e)
    print(email.value, senha.value)
    auth.create_user_with_email_and_password(email.value, senha.value)


def signup(e):
    page_goto(e)
    print(email.value, senha.value)
    # auth.sign_in_with_email_and_password(email.value, senha.value)


def __view__():
    return View(
        "/login",
        [
            ft.Image(
                src="https://archive.org/download/splash-logo/splash-logo.png",
                fit=ft.ImageFit.CONTAIN,
                width=150,
            ),
            ft.Text("Seja Bem Vindo", size=40, weight=ft.FontWeight.BOLD),
            ft.Text("Faça login para continuar", size=18, weight=ft.FontWeight.NORMAL),
            email,
            senha,
            ft.FilledButton(
                text="Entrar",
                on_click=signup,
            ),
            ft.TextButton(
                text="Criar Conta",
                on_click=create_account,
            ),
        ],
    )
