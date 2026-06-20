import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from safety import SafetySystem
class D:
    def __init__(self): self.stopped=False
    def stop(self): self.stopped=True
class S:
    def __init__(self,d): self.d=d
    def read_distance_cm(self): return self.d
d=D(); s=SafetySystem(d,S(10)); assert s.check_and_stop_if_needed()==True; assert d.stopped
print("Safety test passed")
