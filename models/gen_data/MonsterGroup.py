class MonsterGroup():
  def __init__(self, monsters):
    self._monsters = monsters
    self._status = "alive"

  def check_status(self):
    for monster in self._monsters:
      if monster._status == "death_saves":
        self._status = "dead"
        return self._status