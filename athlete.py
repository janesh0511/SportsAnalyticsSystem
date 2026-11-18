from abc import ABC, abstractmethod
from biometric_sensor import BiometricSensor


class Athlete(ABC):

  def __init__(self, athlete_id, full_name):
    self._athlete_id = athlete_id
    self._full_name = full_name
    self._fatigue_index = 0.0
    self._sensor = BiometricSensor(athlete_id)
    self._observers = []

  def rest(self, hours):
    self._fatigue_index = max(0.0, self._fatigue_index - (hours * 5.0))

  def update_hydration(self, liters):
    pass

  def add_observer(self, observer):
    self._observers.append(observer)

  def notify_observers(self):
    if self._fatigue_index > 85.0:
      for obs in self._observers:
        obs.update(self)

  def set_fatigue(self, value):
    self._fatigue_index = min(100.0, max(0.0, value))
    if self._fatigue_index > 85.0:
      self.notify_observers()

  @property
  def fatigue_index(self):
    return self._fatigue_index

  @property
  def full_name(self):
    return self._full_name

  @property
  def athlete_id(self):
    return self._athlete_id

  @abstractmethod
  def calculate_training_load(self, duration_minutes):
    pass

  @abstractmethod
  def get_performance_report(self):
    pass