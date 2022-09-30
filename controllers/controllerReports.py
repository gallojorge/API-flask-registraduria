from Models.reports import Reports
from Repositories.RepositoryReports import RepositoryReports


class ControllerReports:
    def __init__(self):
        self.repositorioReport = RepositoryReports()

    def index(self):
        return self.repositorioReport.findAll()

    def create(self, infoReports):
        nuevoReports = Reports(infoReports)
        return self.repositorioReport.save(nuevoReports)

    def show(self, id):
        elReports = Reports(self.repositorioReport.findById(id))
        return elReports.__dict__

    def update(self, id, infoReports):
        ReportsActual = Reports(self.repositorioReport.findById(id))
        ReportsActual.numerodeMesa = infoReports["numerodeMesa"]
        ReportsActual.partido = infoReports["partido"]
        ReportsActual.nombre = infoReports["nombre"]
        ReportsActual.cantidadVotos = infoReports["cantidadVotos"]
        return self.repositorioReport.save(ReportsActual)

    def delete(self, id):
        return self.repositorioReport.delete(id)
        print("Eliminando con el id")
        return {"deleted_cont": 1}
