
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction fournie 1
class AppFctComp21(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_comp_21.ui", self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_comp_21, "")

        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT R.numEp,AVG(S.age) FROM LesResultats R LEFT OUTER JOIN LesEquipiers E ON (R.numEq=E.numEq) LEFT OUTER JOIN LesSportifs S ON(E.numSp=S.numSp) WHERE R.gold>1 GROUP BY R.numEp")
            

        except Exception as e:
            self.ui.table_fct_comp_21.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_21, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_comp_21, result)


