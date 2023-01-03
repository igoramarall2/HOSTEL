import flet as ft
from flet import (
    AppBar,
    ElevatedButton,
    Page,
    Text,
    View,
    colors,
    Column,
    Row,
    Card,
    Icon,
)
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

nome = ft.TextField(
    label="Nome",
    # hint_text="Seu email para login",
    border=ft.InputBorder.NONE,
    filled=True,
    # width=300,
)
sobrenome = ft.TextField(
    label="Sobrenome",
    border=ft.InputBorder.NONE,
    filled=True,
    # width=300,
)
idade = ft.TextField(
    label="Idade",
    border=ft.InputBorder.NONE,
    filled=True,
    # width=300,
)
email = ft.TextField(
    label="Email",
    border=ft.InputBorder.NONE,
    filled=True,
    # width=300,
)
celular = ft.TextField(
    label="Celular",
    border=ft.InputBorder.NONE,
    filled=True,
    # width=300,
)
data = {
    "nome": nome.value,
    "sobrenome": sobrenome.value,
    "idade": idade.value,
    "email": email.value,
    "celular": celular.value,
}
db.push(data)

t = ft.Tabs(
    selected_index=0,
    animation_duration=300,
    tabs=[
        ft.Tab(
            text="Cadastro",
            icon=ft.icons.ACCOUNT_BOX,
            content=ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.ALBUM),
                                title=ft.Text("The Enchanted Nightingale"),
                                subtitle=ft.Text(
                                    "Music by Julie Gable. Lyrics by Sidney Stein."
                                ),
                            ),
                            ft.Row(
                                [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                            nome,
                            sobrenome,
                            idade,
                            email,
                            celular,
                        ]
                    ),
                    width=400,
                    padding=10,
                )
            ),
        ),
        ft.Tab(
            tab_content=ft.Icon(ft.icons.SEARCH),
            content=ft.Card(
                content=ft.Container(
                    width=500,
                    content=ft.Column(
                        [
                            ft.ListTile(
                                title=ft.Text("One-line list tile"),
                            ),
                            ft.ListTile(
                                title=ft.Text("One-line dense list tile"), dense=True
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.SETTINGS),
                                title=ft.Text("One-line selected list tile"),
                                selected=True,
                            ),
                            ft.ListTile(
                                leading=ft.Image(
                                    src="/icons/icon-192.png", fit="contain"
                                ),
                                title=ft.Text("One-line with leading control"),
                            ),
                            ft.ListTile(
                                title=ft.Text("One-line with trailing control"),
                                trailing=ft.PopupMenuButton(
                                    icon=ft.icons.MORE_VERT,
                                    items=[
                                        ft.PopupMenuItem(text="Item 1"),
                                        ft.PopupMenuItem(text="Item 2"),
                                    ],
                                ),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.ALBUM),
                                title=ft.Text(
                                    "One-line with leading and trailing controls"
                                ),
                                trailing=ft.PopupMenuButton(
                                    icon=ft.icons.MORE_VERT,
                                    items=[
                                        ft.PopupMenuItem(text="Item 1"),
                                        ft.PopupMenuItem(text="Item 2"),
                                    ],
                                ),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.SNOOZE),
                                title=ft.Text(
                                    "Two-line with leading and trailing controls"
                                ),
                                subtitle=ft.Text("Here is a second title."),
                                trailing=ft.PopupMenuButton(
                                    icon=ft.icons.MORE_VERT,
                                    items=[
                                        ft.PopupMenuItem(text="Item 1"),
                                        ft.PopupMenuItem(text="Item 2"),
                                    ],
                                ),
                            ),
                        ],
                        spacing=0,
                    ),
                    padding=ft.padding.symmetric(vertical=10),
                )
            ),
        ),
        ft.Tab(
            text="Tab 3",
            icon=ft.icons.SETTINGS,
            content=ft.Card(
                content=ft.Container(
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("First name")),
                            ft.DataColumn(ft.Text("Last name")),
                            ft.DataColumn(ft.Text("Age"), numeric=True),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("John")),
                                    ft.DataCell(ft.Text("Smith")),
                                    ft.DataCell(ft.Text("43")),
                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Jack")),
                                    ft.DataCell(ft.Text("Brown")),
                                    ft.DataCell(ft.Text("19")),
                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Alice")),
                                    ft.DataCell(ft.Text("Wong")),
                                    ft.DataCell(ft.Text("25")),
                                ],
                            ),
                        ],
                    ),
                    padding=20,
                ),
            ),
        ),
    ],
    expand=1,
)


def __view__():
    return View(
        "/home",
        [ft.Text("Home", size=50, weight=ft.FontWeight.BOLD), t],
    )
