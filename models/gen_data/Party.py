class Party:
    def __init__(self, pcs):
        self._pcs = [pc for pc in pcs]
        for pc in self._pcs:
            pc._party = self
        self._status = "alive"

    def check_status(self):
        dead_count = 0
        for pc in self._pcs:
            if pc._status in ["death_saves", "dead"]:
                dead_count += 1
                
        if dead_count == len(self._pcs):
            self._status = "dead"
        
        return self._status

    def check_party_health(self):
        hps = []
        max_status = 1
        for pc in self._pcs:
            if pc._status != "dead":
                hp_pct = pc._hp / pc._hp_max
                if hp_pct < 0.25: status = 3
                elif hp_pct <= 0.5: status = 2
                else: status = 1

                if status > max_status: max_status = status
                hps.append({"PC": pc, "hp": pc._hp, "status": status})
        
        return hps, max_status
    
    def heal_priority(self):
        priority_list = []
        for pc in self._pcs:
            if pc._status != "dead":
                priority_list.append(pc)
        return sorted(priority_list, key=lambda pc: pc._hp)