class TrainingSquad:

  def __init__(self, squad_name):
    self.squad_name = squad_name
    self.athletes = []

  def add_athlete(self, athlete):
    self.athletes.append(athlete)

  def remove_athlete(self, athlete):
    if athlete in self.athletes:
      self.athletes.remove(athlete)