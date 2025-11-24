from pages.menuPage import menu
import models.data as db


def runApp():
    db.cargarDatos()
    menu()

runApp()