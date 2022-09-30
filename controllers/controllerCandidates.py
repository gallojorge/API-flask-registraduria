from Models.candidates import Candidates
from Models.parties import Parties
from Repositories.RepositoryCandidates import RepositoryCandidates
from Repositories.RepositoryParties import RepositoryParties


class ControllerCandidates:
    def __init__(self):
        self.repositorioCandidates = RepositoryCandidates()
        self.repositorioParties = RepositoryParties()

    def index(self):
        return self.repositorioCandidates.findAll()

    def create(self, infoCandidates):
        nuevoCandidates = Candidates(infoCandidates)
        return self.repositorioCandidates.save(nuevoCandidates)

    def show(self, id):
        elCandidates = Candidates(self.repositorioCandidates.findById(id))
        return elCandidates.__dict__

    def update(self, id, infoCandidates):
        CandidatesActual = Candidates(self.repositorioCandidates.findById(id))
        CandidatesActual.nombre = infoCandidates["nombre"]
        CandidatesActual.apellido = infoCandidates["apellido"]
        CandidatesActual.cedula = infoCandidates["cedula"]
        CandidatesActual.numeroderesolucion = infoCandidates["numeroderesolucion"]
        return self.repositorioCandidates.save(CandidatesActual)

    def delete(self, id):
        return self.repositorioCandidates.delete(id)
    # relación de candidato con partido

    def asignarPartido(self, id, id_parties):
        candidatesActual = Candidates(self.repositorioCandidates.findById(id))
        partiesActual = Parties(self.repositorioParties.findById(id_parties))
        candidatesActual.partie = partiesActual
        return self.repositorioCandidates.save(candidatesActual)
