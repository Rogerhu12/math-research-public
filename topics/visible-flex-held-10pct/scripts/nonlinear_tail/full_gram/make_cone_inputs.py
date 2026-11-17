"""Regenerate finite Fourier test data from the independently defined R10 cone."""
import argparse,importlib.util,json,hashlib
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--cone-source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
spec=importlib.util.spec_from_file_location('cone_exact',a.cone_source);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
N=2048;u=2*np.pi*np.arange(N)/N;freq=2*np.arange(1,33);cs=np.cos(u[:,None]*freq)
rows=[]
for amp in [.0004,.001,.002,.0088]:
 c=mod.ConePlateau(.00358,amp);v=c.evaluate(.25,u);H=2*np.mean(v['X'][:,2,None]*cs,axis=0);mean=float(np.mean(v['Xr'][:,2]));
 rows.append(dict(amplitude=amp,w=c.w,b=c.b,radius=.25,H=H.tolist(),meanSlope=mean,finite_height_linf_error=float(np.max(abs(np.mean(v['X'][:,2])+cs@H-v['X'][:,2])))))
 print(json.dumps({'amplitude':amp,'finite_height_error':rows[-1]['finite_height_linf_error']}),flush=True)
a.out.write_text(json.dumps(dict(scope=__doc__,cone_source_sha256=hashlib.sha256(a.cone_source.read_bytes()).hexdigest(),angles=N,rows=rows),indent=2)+'\n')
