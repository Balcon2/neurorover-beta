import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
import config
config.MOCK_HARDWARE=True
from motor import DriveBase
d=DriveBase(); d.forward(.2); d.left(.2); d.right(.2); d.backward(.2); d.stop()
print("Mock motor test passed")
