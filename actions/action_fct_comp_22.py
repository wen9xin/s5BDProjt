
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction fournie 1
class AppFctComp22(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_comp_22.ui", self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_comp_22, "")

        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT DISTINCT S.pays ,COUNT(R1.gold) as nbGold, COUNT(R1.silver) as silver, COUNT(R1.bronze) as bronze FROM LesSportifs S LEFT OUTER JOIN LesResultats R1 ON (R1.gold=S.numSp OR R1.silver=S.numSp OR R1.bronze=S.numSp) WHERE R1.gold=S.numSp  OR R1.silver=S.numSp OR R1.bronze=S.numSp")
            

        except Exception as e:
            self.ui.table_fct_comp_22.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_22, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_comp_22, result)


