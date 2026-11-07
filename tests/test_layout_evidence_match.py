"""Synthetic lab-observer fields only; no OEM trace, UI, process or device access."""
import subprocess,unittest
from pathlib import Path
HELPER=Path(__file__).resolve().parents[1]/'tools/layout_evidence_match.sh'
def fixture(sid=1000):
 return [f'CA_HOME_GEOMETRY tick=22 id={sid} source=0,0,1920,720 dest=0,0,1280,730 opacity=1.0000 orientation=0 transition=0 duration=300 layer=102',
 'CA_HOME_VIEW tick=22 order=1 xy=0.000,0.000 alpha=1.0000 transform_enabled=1 matrix=0.666667,1.013889,0.000000,0.000031',
 f'CA_FRAME_PROBE tick=22 id={sid} layer=102 visible=1 layer_visible=1 buffer=1920x720 dest=0,0,1280,730 callbacks=0 views=1 listed=1 output=1',
 f'CA_SURFACE_OWNER tick=22 id={sid} pid=4242 comm=AppHomeScreen','4242']
def accepts(fields):
 return subprocess.run(['bash','-c','source "$1"; ca_layout_evidence_match "$2" "$3" "$4" "$5" "$6"','test',str(HELPER),*fields],capture_output=True).returncode==0
class LayoutFields(unittest.TestCase):
 def test_original_assignment(self):self.assertTrue(accepts(fixture()))
 def test_reordered_assignment(self):self.assertTrue(accepts(fixture(1001)))
 def test_wrong_owner(self):
  f=fixture(1001);f[3]=f[3].replace('AppHomeScreen','AppStandbyClock');self.assertFalse(accepts(f))
 def test_wrong_pid(self):
  f=fixture();f[4]='4243';self.assertFalse(accepts(f))
 def test_wrong_surface(self):
  f=fixture(1001);f[2]=f[2].replace('id=1001','id=1000');self.assertFalse(accepts(f))
 def test_stale_frame(self):
  f=fixture();f[2]=f[2].replace('tick=22','tick=21');self.assertFalse(accepts(f))
 def test_wrong_scale(self):
  f=fixture();f[1]=f[1].replace('matrix=0.666667','matrix=1.000000');self.assertFalse(accepts(f))
 def test_clipped_destination(self):
  f=fixture();f[0]=f[0].replace('dest=0,0,1280,730','dest=0,0,1920,720');self.assertFalse(accepts(f))
 def test_hidden(self):
  f=fixture();f[2]=f[2].replace('visible=1 ','visible=0 ',1);self.assertFalse(accepts(f))
if __name__=='__main__':unittest.main()
