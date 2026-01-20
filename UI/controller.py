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
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN

    def popola_dropdown_musei(self):
        self._view.dropdown_musei.options.clear()
        self._view.dropdown_musei.options.append(ft.dropdown.Option(key=None, text='Nessun filtro'))

        musei = self._model.get_musei()

        if musei:
            for museo in musei:
                self._view.dropdown_musei.options.append(ft.dropdown.Option(museo.nome))
        else:
            self._view.show_alert("Errore nel caricamento musei")

        self._view.update()


    def popola_dropdown_epoca(self):
        self._view.dropdown_epoca.options.clear()
        self._view.dropdown_epoca.options.append(ft.dropdown.Option(key=None, text='Nessun filtro'))

        epoche = self._model.get_epoche()

        if epoche:
            for epoca in epoche:
                self._view.dropdown_epoca.options.append(ft.dropdown.Option(epoca))
        else:
            self._view.show_alert("Errore nel caricamento epoche")

        self._view.update()


    # CALLBACKS DROPDOWN

    def on_museo_change(self, e):
        valore = e.control.value
        if valore == "Nessun filtro":
            self.museo_selezionato = None
        else:
            self.museo_selezionato = valore

    def on_epoca_change(self, e):
        valore = e.control.value
        if valore == "Nessun filtro":
            self.epoca_selezionata = None
        else:
            self.epoca_selezionata = valore


    # AZIONE: MOSTRA ARTEFATTI

    def handler_mostra_artefatti(self, e):

        museo = self.museo_selezionato
        epoca = self.epoca_selezionata

        self._view.lista_artefatti.controls.clear()
        lista_artefatti = self._model.get_artefatti_filtrati(museo, epoca)

        if lista_artefatti is None:
            self._view.show_alert("Errore di connessione al database.")
        elif len(lista_artefatti) == 0:
            self._view.show_alert("Nessun artefatto trovato per i criteri selezionati")
        else:
            for artefatto in lista_artefatti:
                self._view.lista_artefatti.controls.append(ft.Text(f"{artefatto}"))

        self._view.update()

