class PerformanceAnalyticsHub:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(PerformanceAnalyticsHub, cls).__new__(cls)
      cls._instance.squads = []
    return cls._instance

  def register_squad(self, squad):
    self.squads.append(squad)

  def generate_facility_report(self):
    report = "=== FACILITY-WIDE PERFORMANCE REPORT ===\n"
    for squad in self.squads:
      report += f"Squad: {squad.squad_name}\n"
      for ath in squad.athletes:
        report += f"  - {ath.get_performance_report()}\n"
    return report