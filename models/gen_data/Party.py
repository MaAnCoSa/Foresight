class Party:
    def __init__(self, pcs):
        self._pcs = [pc for pc in pcs]
        self._status = "alive"

    def check_status(self):
        dead_count = 0
        for pc in self._pcs:
            if pc._status == "death_saves":
                dead_count += 1
                
        if dead_count == len(self._pcs):
            self._status = "dead"
        
        return self._status
