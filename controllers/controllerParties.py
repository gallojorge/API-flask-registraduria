from Models.parties import Parties
from Repositories.RepositoryParties import RepositoryParties


class ControllerParties:
    def __init__(self):
        self.repositorioParties = RepositoryParties()

    def index(self):
        return self.repositorioParties.findAll()

    def create(self, infoParties):
        nuevoParties = Parties(infoParties)
        return self.repositorioParties.save(nuevoParties)

    def show(self, id):
        elParties = Parties(self.repositorioParties.findById(id))
        return elParties.__dict__

    def update(self, id, infoParties):
        PartiesActual = Parties(self.repositorioParties.findById(id))
        PartiesActual.codeparties = infoParties["codeparties"]
        PartiesActual.name = infoParties["name"]
        PartiesActual.lema = infoParties["lema"]
        PartiesActual.logo = infoParties["logo"]
        return self.repositorioParties.save(PartiesActual)

    def delete(self, id):
        return self.repositorioParties.delete(id)
        print("Eliminando con el id")
        return {"deleted_cont": 1}
