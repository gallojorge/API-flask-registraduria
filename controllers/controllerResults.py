from Models.results import Results
from Repositories.RepositoryResults import RepositoryResults


class ControllerResults:
    def __init__(self):
        self.repositorioResults = RepositoryResults()

    def index(self):
        return self.repositorioResults.findAll()

    def create(self, infoResults):
        nuevoResults = Results(infoResults)
        return self.repositorioResults.save(nuevoResults)

    def show(self, id):
        results = Results(self.repositorioResults.findById(id))
        return results.__dict__

    def update(self, id, infoResults):
        resultadoActual = Results(self.repositorioResults.findById(id))
        resultadoActual.numeroVotos = infoResults["numeroVotos"]
        return self.repositorioResults.save(resultadoActual)

    def delete(self, id):
        return self.repositorioResults.delete(id)
