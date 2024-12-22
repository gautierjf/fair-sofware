from constraint import Problem
from model.objects.table import Table

class ComputeUsecase:
  def __init__(self, room,tableGroup,distanceFromTheWall, numberOfAlleys,widthAlley):
    self.room = room
    self.tableGroup = tableGroup
    self.distanceFromTheWall = distanceFromTheWall
    self.numberOfAlleys = numberOfAlleys
    self.widthAlley = widthAlley

  def execute(self):
    usableLength = self.room.length - 2 * self.distanceFromTheWall
    usableWidth = self.room.width - 2 * self.distanceFromTheWall

    # Largeur totale occupée par les allées
    allWidthAlleys = self.numberOfAlleys * self.widthAlley

    # Largeur disponible pour les rows de tables
    widthAvaibleForTables = usableWidth - allWidthAlleys

    if widthAvaibleForTables <= 0:
        return 0, []  # Pas d'espace pour les tables

    # Définir le problème de contrainte
    problem = Problem()

    # Calcul du nombre maximal de tables en orientation horizontale par rangée
    maxTableByHorizontalRow = max(1, int(usableLength / int(self.tableGroup.length)))

    # Calcul du nombre maximal de rows en orientation horizontale
    maxHorizontalRow = max(1, int(widthAvaibleForTables / int(self.tableGroup.width)))

    # Calcul du nombre maximal de tables en orientation verticale par rangée
    maxTableByVerticalRow = max(1, int(usableLength / int(self.tableGroup.width)))

    # Calcul du nombre maximal de rows en orientation verticale
    maxVerticalRow = max(1, int(widthAvaibleForTables / int(self.tableGroup.length)))
    
    if maxTableByHorizontalRow > 0 and maxHorizontalRow > 0:
        problem.addVariable("tablesByHorizontalRow", range(1, maxTableByHorizontalRow + 1))
        problem.addVariable("horizontalRows", range(1, maxHorizontalRow + 1))
        
    if maxTableByVerticalRow > 0 and maxVerticalRow > 0:
        problem.addVariable("tablesByVerticalRow", range(1, maxTableByVerticalRow + 1))
        problem.addVariable("verticalRows", range(1, maxVerticalRow + 1))

    # Ajouter une contrainte sur l'espace total occupé pour chaque orientation
    def horizontalUseSpace(tablesByRow, rows):
        return (tablesByRow * self.tableGroup.length) <= usableLength and (rows * self.tableGroup.width) <= widthAvaibleForTables

    def verticalUseSpace(tablesByRow, rows):
        return (tablesByRow * self.tableGroup.width) <= usableLength and (rows * self.tableGroup.length) <= widthAvaibleForTables

    problem.addConstraint(horizontalUseSpace, ["tablesByHorizontalRow", "horizontalRows"])
    problem.addConstraint(verticalUseSpace, ["tablesByVerticalRow", "verticalRows"])
    
    solutions = problem.getSolutions()

    # Calculer le nombre total maximal de tables et leurs positions
    max_tables = 0
    best_solution = None

    for solution in solutions:
        total_tables_horizontale = solution.get("tablesByHorizontalRow", 0) * solution.get("horizontalRows", 0)
        total_tables_verticale = solution.get("tablesByVerticalRow", 0) * solution.get("verticalRows", 0)

        if total_tables_horizontale > max_tables:
            max_tables = total_tables_horizontale
            best_solution = ("horizontale", solution["tablesByHorizontalRow"], solution["horizontalRows"])

        if total_tables_verticale > max_tables:
            max_tables = total_tables_verticale
            best_solution = ("verticale", solution["tablesByVerticalRow"], solution["verticalRows"])

    # Générer les coordonnées des tables
    tables = []
    if best_solution:
        orientation, tablesByRow, rows = best_solution

        for i in range(rows):
            for j in range(tablesByRow):
                if orientation == "horizontale":
                    x = self.distanceFromTheWall + j * self.tableGroup.length + self.widthAlley
                    y = self.distanceFromTheWall + i * self.tableGroup.width
                    table = Table(len(tables)+1,self.room.name+str(i)+str(j),self.room,self.tableGroup,x,y,"Horizontal")
                    tables.append(table)

                else:  # verticale
                    x = self.distanceFromTheWall + j * self.tableGroup.width + self.widthAlley
                    y = self.distanceFromTheWall + i * self.tableGroup.length
                    table = Table(len(tables)+1,self.room.name+str(i)+str(j),self.room,self.tableGroup,x,y,"Vertical")
                    tables.append(table)
    
    return tables

