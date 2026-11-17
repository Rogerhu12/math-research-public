import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
import json,numpy as np
from scipy.integrate import quad
from even_mode_loader import load,module
root=Path('/workspace/scratch/f00f08c94d46');here=root/'even_plateau_work';src=root/'m3_flat17_work/recovered/bundle/topics/visible-flexible-closed-surface'
ad=load(src,4);module('circle_check_bridge',src.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py').install();p=json.load(open(here/'mode4_port8.json'));rows=[]
for name in ['vu17-vd18','vu25-vd30']:
 cfg=json.load(open(here/name/'profile.json'));chart=json.load(open(here/name/'chart.json'));p['cut']['_prefix_bridge']=cfg['prefix_bridge'];Flow,_=ad.build_classes(chart);f=Flow(cfg,p,4,.045,128,4,warp_q=.045);k=40/13
 # Acceleration pieces before first nonpositive-a'' band, exact profile endpoints.
 def v(s):
  a,ap,app=[float(x)for x in f.profile(np.array([s]))];return np.sqrt(max(app,0)/(a*(k*k-ap*ap)))
 cuts=sorted(set([0.,float(f.Tu)]+[float(x)for x in f.breaks if 0<x<f.Tu]));loss=sum(quad(v,lo,hi,epsabs=1e-11,limit=100)[0]for lo,hi in zip(cuts,cuts[1:]));row=dict(profile=name,Tu=f.Tu,delta=cfg['delta'],sampled_characteristic_loss=loss,required_halfwidth=.325*.28,scope='Numerical characteristic diagnostic only, no existence or interval claim');rows.append(row)
print(json.dumps(rows,indent=2));(here/'circle_consumption.json').write_text(json.dumps(rows,indent=2)+'\n')
