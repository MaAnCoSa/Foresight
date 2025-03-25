class MonsterGroup():
  def __init__(self, monsters):
    self._monsters = monsters
    self._status = "alive"
      
  def check_status(self):
        dead_count = 0
        for monster in self._monsters:
            if monster._status == "dead":
                dead_count += 1
                
        if dead_count == len(self._monsters):
            self._status = "dead"
        
        return self._status