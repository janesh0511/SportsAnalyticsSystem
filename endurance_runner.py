from athlete import Athlete


class EnduranceRunner(Athlete):

  def __init__(self, athlete_id, full_name, vo2_max, preferred_pace):
    super().__init__(athlete_id, full_name)
    self._vo2_max = vo2_max
    self._preferred_pace = preferred_pace

  def calculate_training_load(self, duration_minutes):
    load = duration_minutes * (self._vo2_max / 50.0) ** 1.5
    return round(load, 2)

  def get_performance_report(self):
    return (
        f"Endurance Runner {self._full_name} (ID: {self._athlete_id})  VO2"
        f" Max: {self._vo2_max} | Pace: {self._preferred_pace} min/km  Fatigue:"
        f" {self._fatigue_index:.1f}%"
    )