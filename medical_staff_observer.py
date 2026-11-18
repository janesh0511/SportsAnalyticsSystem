class MedicalStaffObserver:

  def __init__(self, staff_name):
    self.staff_name = staff_name

  def update(self, athlete):
    print(
        f"\n[ALERT - {self.staff_name}] High fatigue detected for"
        f" {athlete.full_name} ({athlete.athlete_id}):"
        f" {athlete.fatigue_index:.1f}%!\n"
    )