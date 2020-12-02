
import sqlite3
from utils import db
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction à compléter 1
class AppFctComp31(QDialog):

    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_comp_31.ui", self)
        self.data = data
        self.refreshResult()

    @pyqtSlot()
    def refreshResult(self):
        display.refreshLabel(self.ui.label_fct_comp_31, "ref")

    @pyqtSlot()
    def Ajouter(self):

        display.refreshLabel(self.ui.label_fct_comp_31, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute("INSERT INTO LesInscriptions (numIn, numEp) VALUES (?, ?) ",
                                    [self.ui.lineEdit_31_a_in.text().strip(), self.ui.lineEdit_31_a_ep.text().strip()])
        except Exception as e:
            display.refreshLabel(self.ui.label_fct_comp_31, "Impossible d'ajouter  : " + repr(e))
        else:
            display.refreshLabel(self.label_fct_comp_31, "Une ligne a été inséré dans la base avec succès.")
            self.data.commit()
            # On émet le signal indiquant la modification de la table

    def Suppr(self):

        display.refreshLabel(self.ui.label_fct_comp_31, "")
        try:
            db.updateDBfile(self.data, "DELETE FROM LesInscriptions WHERE numIn= ?  AND numEp= ? ) ",[self.ui.lineEdit_31_a_in.text().strip()],[self.ui.lineEdit_31_a_ep.text().strip()])
        except Exception as e:
            display.refreshLabel(self.ui.label_fct_comp_31, "Impossible d'ajouter  : " + repr(e))
        else:
            display.refreshLabel(self.label_fct_comp_31, "Une ligne a été supprime dans la base avec succès.")
            self.data.commit()
            # On émet le signal indiquant la modification de la table
