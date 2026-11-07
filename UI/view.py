import flet as ft
from flet.controls import border

from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None
        self.biblioteche = []
        self.generi = []

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO

        # Sezione 3: Libri
        # TODO

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        self.ddBiblioteche = ft.Dropdown(hint_text="Biblioteca", label="Biblioteche di Torino", width=300)
        self.ddGeneri = ft.Dropdown(hint_text="Genere", label="Genere Libro", width=200)
        self.btnLibri = ft.Button("Mostra Libri", on_click=self.controller.filtra_libri)
        self.listaLibri = ft.ListView(expand=True, spacing=10)


        self.biblioteche = self.controller.get_biblioteche()
        self.generi = self.controller.get_generi()

        self.ddBiblioteche.options.append(ft.DropdownOption("Nessun Filtro"))
        self.ddGeneri.options.append(ft.DropdownOption("Nessun Filtro"))


        for elem in self.biblioteche:
            self.ddBiblioteche.options.append(ft.DropdownOption(key=elem.id, text=elem.nome))

        for elem in self.generi:
            self.ddGeneri.options.append(ft.DropdownOption(elem))

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(controls=[self.ddBiblioteche, self.ddGeneri], spacing=170, alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Libri
            self.btnLibri,
            ft.Divider(),
            self.listaLibri,

        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

    def aggiorna_libri(self, libri):
        self.listaLibri.controls.clear()

        if not libri:
            self.show_alert("LIBRI NON TROVATI")
        else:
            for libro in libri:
                txt_libro = str(libro)
                self.listaLibri.controls.append(ft.Text(value=txt_libro))

        self.listaLibri.update()
