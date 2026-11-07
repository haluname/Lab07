import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def get_biblioteche(self):
        biblioteche = self._model.get_biblioteche()
        return biblioteche

    def get_generi(self):
        generi = self._model.get_generi()
        return generi


    # AZIONE: MOSTRA LIBRI
    def filtra_libri(self):
        self.biblioteca_selezionata = self._view.ddBiblioteche.value
        self.genere_selezionato = self._view.ddGeneri.value
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        self._view.aggiorna_libri(libri)