from Models.candidates import Candidates
from Models.tables import Tables

from Repositories.RepositoryTables import RepositoryTables
from Repositories.RepositoryCandidates import RepositoryCandidates


class ControllerTables:
    def __init__(self):
        self.repositorioTables = RepositoryTables()
        self.repositorioCandidates = RepositoryCandidates()

    def index(self):
        return self.repositorioTables.findAll()

    def create(self, infoTables):
        nuevoTables = Tables(infoTables)
        return self.repositorioTables.save(nuevoTables)

    def show(self, id):
        elTables = Tables(self.repositorioTables.findById(id))
        return elTables.__dict__

    def update(self, id, infoTables):
        TablesActual = Tables(self.repositorioTables.findById(id))
        TablesActual.numeroMesas = infoTables["numeroMesa"]
        TablesActual.cedulasInscritas = infoTables["cedulasInscritas"]
        return self.repositorioTables.save(TablesActual)

    def delete(self, id):
        return self.repositorioTables.delete(id)

    def asignarCandidates(self, id, id_candidates):
        TablesActual = Tables(self.repositorioTables.findById(id))
        candidatesActual = Candidates(
            self.repositorioCandidates.findById(id_candidates)
        )
        TablesActual.candidates = (
            candidatesActual  # partie es el nombre del nuevo objeto
        )
        return self.repositorioTables.save(TablesActual)
