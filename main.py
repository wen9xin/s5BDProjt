
import sys, sqlite3
from utils import db
from utils import display
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
from actions.action_tablesData import AppTablesData
from actions.action_fct_fournie_1 import AppFctFournie1
from actions.action_fct_fournie_2 import AppFctFournie2
from actions.action_fct_comp_1 import AppFctComp1
from actions.action_fct_comp_11 import AppFctComp11
from actions.action_fct_comp_12 import AppFctComp12
from actions.action_fct_comp_13 import AppFctComp13
from actions.action_fct_comp_21 import AppFctComp21
from actions.action_fct_comp_22 import AppFctComp22
from actions.action_fct_comp_31 import AppFctComp31
from actions.action_fct_comp_32 import AppFctComp32
from actions.action_fct_comp_2 import AppFctComp2
from actions.action_fct_comp_3 import AppFctComp3
from actions.action_fct_comp_4 import AppFctComp4

# Classe utilisée pour lancer la fenêtre principale de l'application et définir ses actions
class AppWindow(QMainWindow):

    # Création d'un signal destiné à être émis lorsque la table est modifiée
    changedValue = pyqtSignal()

    # TODO 2 : ajouter les fenetres (répertoire gui) et les actions (répertoire actions) correspondant aux 2 items de
    #  la partie 2. TODO 3 : ajouter les fenetres (rep. gui) et les actions (rep. actions) correspondant aux 2 items
    #   de la partie 3.

    # On prévoit des variables pour accueillir les fenêtres supplémentaires
    tablesDataDialog = None
    fct_fournie_1_dialog = None
    fct_fournie_2_dialog = None
    fct_comp_1_dialog = None
    fct_comp_11_dialog = None
    fct_comp_12_dialog = None
    fct_comp_13_dialog = None
    fct_comp_21_dialog = None
    fct_comp_22_dialog = None
    fct_comp_31_dialog = None
    fct_comp_32_dialog = None
    fct_comp_2_dialog = None
    fct_comp_3_dialog = None
    fct_comp_4_dialog = None

    # Constructeur
    def __init__(self):

        # On appelle le constructeur de la classe dont on hérite
        super(AppWindow, self).__init__()

        # On charge le gui de la fenêtre
        self.ui = uic.loadUi("gui/mainWindow.ui", self)

        # On se connecte à la base de données
        self.data = sqlite3.connect("data/jo.db")

    ####################################################################################################################
    # Définition des actions
    ####################################################################################################################

    # Action en cas de clic sur le bouton de création de base de données
    def createDB(self):

        try:
            # On exécute les requêtes du fichier de création
            db.updateDBfile(self.data, "data/createDB.sql")
            display.refreshLabel(self.ui.label_2,"L'erreur 1.")

        except Exception as e:
            # En cas d'erreur, on affiche un message
            display.refreshLabel(self.ui.label_2, "L'erreur suivante s'est produite pendant lors de la création de la base : "+repr(e)+".")

        else:
            # Si tout s'est bien passé, on affiche le message de succès et on commit
            display.refreshLabel(self.ui.label_2, "La base de données a été créée avec succès.")
            self.data.commit()
            # On émet le signal indiquant la modification de la table
            self.changedValue.emit()

    # En cas de clic sur le bouton d'insertion de données
    def insertDB(self):

        try:
            # On exécute les requêtes du fichier d'insertion
            db.updateDBfile(self.data, "data/insertDB.sql")

        except Exception as e:
            # En cas d'erreur, on affiche un message
            display.refreshLabel(self.ui.label_2, "L'erreur suivante s'est produite lors de l'insertion des données : "+repr(e)+".")

        else:
            # Si tout s'est bien passé, on affiche le message de succès et on commit
            display.refreshLabel(self.ui.label_2, "Un jeu de test a été inséré dans la base avec succès.")
            self.data.commit()
            # On émet le signal indiquant la modification de la table
            self.changedValue.emit()

    # En cas de clic sur le bouton de suppression de la base
    def deleteDB(self):

        try:
            # On exécute les requêtes du fichier de suppression
            db.updateDBfile(self.data, "data/deleteDB.sql")

        except Exception as e:
            # En cas d'erreur, on affiche un message
            display.refreshLabel(self.ui.label_2, "Erreur lors de la suppression de la base de données : " + repr(e)+".")

        else:
            # Si tout s'est bien passé, on affiche le message de succès (le commit est automatique pour un DROP TABLE)
            display.refreshLabel(self.ui.label_2, "La base de données a été supprimée avec succès.")
            # On émet le signal indiquant la modification de la table
            self.changedValue.emit()

    ####################################################################################################################
    # Ouverture des autres fenêtres de l'application
    ####################################################################################################################

    # TODO 2 : ajouter la définition des méthodes déclenchées lors des clicks sur les boutons de la partie 2
    # TODO 3 : ajouter la définition des méthodes déclenchées lors des clicks sur les boutons de la partie 3

    # En cas de clic sur le bouton de visualisation des données
    def openData(self):
        if self.tablesDataDialog is not None:
            self.tablesDataDialog.close()
        self.tablesDataDialog = AppTablesData(self.data)
        self.tablesDataDialog.show()
        self.changedValue.connect(self.tablesDataDialog.refreshAllTables)

    # En cas de clic sur la fonction fournie 1
    def open_fct_fournie_1(self):
        if self.fct_fournie_1_dialog is not None:
            self.fct_fournie_1_dialog.close()
        self.fct_fournie_1_dialog = AppFctFournie1(self.data)
        self.fct_fournie_1_dialog.show()
        self.changedValue.connect(self.fct_fournie_1_dialog.refreshResult)

    # En cas de clic sur la fonction fournie 2
    def open_fct_fournie_2(self):
        if self.fct_fournie_2_dialog is not None:
            self.fct_fournie_2_dialog.close()
        self.fct_fournie_2_dialog = AppFctFournie2(self.data)
        self.fct_fournie_2_dialog.show()

    # En cas de clic sur la fonction à compléter 1
    def open_fct_comp_1(self):
        if self.fct_comp_1_dialog is not None:
            self.fct_comp_1_dialog.close()
        self.fct_comp_1_dialog = AppFctComp1(self.data)
        self.fct_comp_1_dialog.show()
        self.changedValue.connect(self.fct_comp_1_dialog.refreshResult)

    def open_fct_comp_11(self):
        if self.fct_comp_11_dialog is not None:
            self.fct_comp_11_dialog.close()
        self.fct_comp_11_dialog = AppFctComp11(self.data)
        self.fct_comp_11_dialog.show()
        self.changedValue.connect(self.fct_comp_11_dialog.refreshResult)

    def open_fct_comp_12(self):
        if self.fct_comp_12_dialog is not None:
            self.fct_comp_12_dialog.close()
        self.fct_comp_12_dialog = AppFctComp12(self.data)
        self.fct_comp_12_dialog.show()
        self.changedValue.connect(self.fct_comp_12_dialog.refreshResult)

    def open_fct_comp_13(self):
        if self.fct_comp_13_dialog is not None:
            self.fct_comp_13_dialog.close()
        self.fct_comp_13_dialog = AppFctComp13(self.data)
        self.fct_comp_13_dialog.show()
        self.changedValue.connect(self.fct_comp_13_dialog.refreshResult)

    def open_fct_comp_21(self):
        if self.fct_comp_21_dialog is not None:
            self.fct_comp_21_dialog.close()
        self.fct_comp_21_dialog = AppFctComp21(self.data)
        self.fct_comp_21_dialog.show()
        self.changedValue.connect(self.fct_comp_21_dialog.refreshResult)

    def open_fct_comp_22(self):
        if self.fct_comp_22_dialog is not None:
            self.fct_comp_22_dialog.close()
        self.fct_comp_22_dialog = AppFctComp22(self.data)
        self.fct_comp_22_dialog.show()
        self.changedValue.connect(self.fct_comp_22_dialog.refreshResult)

    def open_fct_comp_31(self):
        if self.fct_comp_31_dialog is not None:
            self.fct_comp_31_dialog.close()
        self.fct_comp_31_dialog = AppFctComp31(self.data)
        self.fct_comp_31_dialog.show()
        self.changedValue.connect(self.fct_comp_31_dialog.refreshResult)

    def open_fct_comp_32(self):
        if self.fct_comp_32_dialog is not None:
            self.fct_comp_32_dialog.close()
        self.fct_comp_32_dialog = AppFctComp32(self.data)
        self.fct_comp_32_dialog.show()
        self.changedValue.connect(self.fct_comp_32_dialog.refreshResult)

    # En cas de clic sur la fonction à compléter 2
    def open_fct_comp_2(self):
        if self.fct_comp_2_dialog is not None:
            self.fct_comp_2_dialog.close()
        self.fct_comp_2_dialog = AppFctComp2(self.data)
        self.fct_comp_2_dialog.show()

    # En cas de clic sur la fonction à compléter 3
    def open_fct_comp_3(self):
        if self.fct_comp_3_dialog is not None:
            self.fct_comp_3_dialog.close()
        self.fct_comp_3_dialog = AppFctComp3(self.data)
        self.fct_comp_3_dialog.show()

    # En cas de clic sur la fonction à compléter 4
    def open_fct_comp_4(self):
        if self.fct_comp_4_dialog is not None:
            self.fct_comp_4_dialog.close()
        self.fct_comp_4_dialog = AppFctComp4(self.data)
        self.fct_comp_4_dialog.show()
        self.changedValue.connect(self.fct_comp_4_dialog.refreshCatList)

    ####################################################################################################################
    # Fonctions liées aux évènements (signal/slot/event)
    ####################################################################################################################

    # TODO 2 : penser à fermer comme il faut les fenêtres de la partie 2
    # TODO 3 : penser à fermer comme il faut les fenêtres de la partie 3

    # On intercepte l'évènement de cloture de la fenêtre principale pour intercaler quelques actions avant sa fermeture
    def closeEvent(self, event):

        # On ferme les éventuelles fenêtres encore ouvertes
        if (self.tablesDataDialog is not None):
            self.tablesDataDialog.close()
        if (self.fct_fournie_1_dialog is not None):
            self.fct_fournie_1_dialog.close()
        if (self.fct_fournie_2_dialog is not None):
            self.fct_fournie_2_dialog.close()
        if (self.fct_comp_1_dialog is not None):
            self.fct_comp_1_dialog.close()
        if (self.fct_comp_11_dialog is not None):
            self.fct_comp_11_dialog.close()
        if (self.fct_comp_12_dialog is not None):
            self.fct_comp_12_dialog.close()
        if (self.fct_comp_13_dialog is not None):
            self.fct_comp_13_dialog.close()
        if (self.fct_comp_21_dialog is not None):
            self.fct_comp_21_dialog.close()
        if (self.fct_comp_22_dialog is not None):
            self.fct_comp_22_dialog.close()
        if (self.fct_comp_31_dialog is not None):
            self.fct_comp_31_dialog.close()
        if (self.fct_comp_32_dialog is not None):
            self.fct_comp_32_dialog.close()
        if (self.fct_comp_2_dialog is not None):
            self.fct_comp_2_dialog.close()
        if (self.fct_comp_3_dialog is not None):
            self.fct_comp_3_dialog.close()
        if (self.fct_comp_4_dialog is not None):
            self.fct_comp_4_dialog.close()

        # On ferme proprement la base de données
        self.data.close()

        # On laisse l'évènement de clôture se terminer normalement
        event.accept()

# Lancement de la fenêtre principale
app = QApplication(sys.argv)
MainWindow = AppWindow()
MainWindow.show()
sys.exit(app.exec_())