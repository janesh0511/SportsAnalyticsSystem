from athlete import Athlete


class Weightlifter(Athlete):

  def __init__(self, athlete_id, full_name, one_rep_max_kg, weight_class_kg):
    super().__init__(athlete_id, full_name)
    self._one_rep_max_kg = one_rep_max_kg
    self._weight_class_kg = weight_class_kg

  def calculate_training_load(self, duration_minutes):
    load = duration_minutes * (self._one_rep_max_kg / 100.0) * 0.8
    return round(load, 2)

  def record_session(self, sets, reps, weight_used_kg=None):
    if weight_used_kg is None:
      weight_used_kg = self._one_rep_max_kg * 0.75
    intensity_pct = (weight_used_kg / self._one_rep_max_kg) * 100
    load = sets * reps * (intensity_pct / 10.0)
    new_fatigue = self._fatigue_index + (sets * reps * 0.6)
    self.set_fatigue(new_fatigue)
    return round(load, 2)

  def get_performance_report(self):
    return (
        f"Weightlifter {self._full_name} (ID: {self._athlete_id})  1RM:"
        f" {self._one_rep_max_kg}kg | Class: {self._weight_class_kg}kg "
        f" Fatigue: {self._fatigue_index:.1f}%"
    )