
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction à compléter 1
class AppFctComp31(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_comp_31.ui", self)
        self.data = data


    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def Ajouter(self):

        display.refreshLabel(self.ui.label_fct_comp_31, "")
        if not self.ui.a_ep.text().strip() or not self.ui.a_in.text().strip():
            display.refreshLabel(self.ui.label_fct_comp_31, "Veuillez indiquer les numéro")
        else:
            try:
                cursor = self.data.cursor()
                result = cursor.execute("INSERT INTO LesInscriptions (numIn, numEp) VALUES (?, ?); ", [self.ui.a_in.text().strip()],[self.ui.a_ep.text().strip()])
            except Exception as e:
                display.refreshLabel(self.ui.label_fct_comp_31, "Impossible d'afficher les résultats : " + repr(e))
            else:
                i = display.refreshGenericData(self.ui.table_fct_comp_31, result)
                if i == 0:
                    display.refreshLabel(self.ui.label_fct_comp_31, "Aucun résultat")