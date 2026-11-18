class BiometricSensor:

  def __init__(self, athlete_id):
    self.athlete_id = athlete_id
    self.heart_rate = 72.0
    self.oxygen_saturation = 98.0

  def update_readings(self, hr, o2):
    self.heart_rate = hr
    self.oxygen_saturation = o2