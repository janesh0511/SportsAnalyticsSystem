from endurance_runner import EnduranceRunner
from weightlifter import Weightlifter


class AthleteFactory:

  @staticmethod
  def create_athlete(sport_type, athlete_id, name):
    if sport_type.lower() == "runner":
      return EnduranceRunner(athlete_id, name, vo2_max=55.0, preferred_pace=4.2)
    elif sport_type.lower() == "weightlifter":
      return Weightlifter(
          athlete_id, name, one_rep_max_kg=140.0, weight_class_kg=81.0
      )
    else:
      raise ValueError(f"Unknown sport type: {sport_type}")