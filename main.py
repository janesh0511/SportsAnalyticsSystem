from athlete_factory import AthleteFactory
from medical_staff_observer import MedicalStaffObserver
from performance_analytics_hub import PerformanceAnalyticsHub
from training_squad import TrainingSquad


def main():
  hub = PerformanceAnalyticsHub()
  medic = MedicalStaffObserver("Dr. Roberts")
  olympic_squad = TrainingSquad("Elite Olympic Squad")

  runner = AthleteFactory.create_athlete("runner", "A101", "Janesh S.")
  lifter = AthleteFactory.create_athlete("weightlifter", "A102", "Marcus Vance")

  runner.add_observer(medic)
  lifter.add_observer(medic)

  olympic_squad.add_athlete(runner)
  olympic_squad.add_athlete(lifter)
  hub.register_squad(olympic_squad)

  print("--- Testing Polymorphic Training Load Calculations ---")
  for athlete in olympic_squad.athletes:
    load = athlete.calculate_training_load(60)
    print(f"{athlete.full_name} Load (60 mins): {load}")

  print("\n--- Testing Overloaded Sessions & Fatigue Alerts ---")
  lifter.record_session(sets=3, reps=10, weight_used_kg=100.0)
  print(lifter.get_performance_report())

  print("Pushing lifter to high fatigue...")
  lifter.record_session(sets=12, reps=10, weight_used_kg=130.0)

  print("\n--- Global Analytics Hub Report ---")
  print(hub.generate_facility_report())


if __name__ == "__main__":
  main()