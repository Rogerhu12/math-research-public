"""Compare actual finite Cartesian derivative jets on a common physical sample grid."""
import argparse,gzip,hashlib,json
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('inputs',nargs='+',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args();records=[]
for f in a.inputs:
 d=json.loads(gzip.decompress(f.read_bytes()));d['_file']=str(f);d['_sha']=hashlib.sha256(f.read_bytes()).hexdigest();records.append(d)
keys=['Xr','Xu','Xrr','Xru','Xuu'];rows=[]
for x,y in zip(records[:-1],records[1:]):
 assert len(x['samples'])==len(y['samples']);xx=np.array([s['jets']for s in x['samples']]);yy=np.array([s['jets']for s in y['samples']]);assert xx.shape==yy.shape
 for s,t in zip(x['samples'],y['samples']):
  assert all(s[k]==t[k]for k in ['stage','x']) and abs(s['r']-t['r'])<1e-13 and abs(s['w']-t['w'])<1e-13
 delta=np.linalg.norm(yy-xx,axis=-1);radii=np.array([s['r']for s in x['samples']])[:,None];E=1+np.array([s['w']for s in x['samples']])[:,None]**2
 # Orthonormal connection Hessian differences in the same fixed g.
 dR=yy[:,:,0]-xx[:,:,0];dT=yy[:,:,1]-xx[:,:,1];dRR=yy[:,:,2]-xx[:,:,2];dRT=yy[:,:,3]-xx[:,:,3];dTT=yy[:,:,4]-xx[:,:,4]
 # H1 needs w_r, omitted from saved compact grid; raw rr is reported instead.
 H2=(dRT-dT/radii[:,:,None])/(radii[:,:,None]*np.sqrt(E)[:,:,None]);H3=dTT/radii[:,:,None]**2+dR/(E*radii)[:,:,None]
 worst=[]
 for j,k in enumerate(keys):
  loc=np.unravel_index(np.argmax(delta[:,:,j]),delta[:,:,j].shape);s=x['samples'][loc[0]];worst.append(dict(derivative=k,max_norm=float(delta[loc[0],loc[1],j]),where={z:s[z]for z in ['stage','rawCell','rawSegment','x','r','w']},angular_index=int(loc[1])))
 rows.append(dict(from_M=x['M'],to_M=y['M'],maximum_derivative_differences=worst,orthonormal_mixed_hessian_difference_max=float(np.max(np.linalg.norm(H2,axis=-1))),orthonormal_angular_hessian_difference_max=float(np.max(np.linalg.norm(H3,axis=-1)))))
report=dict(scope=__doc__,limitations=['Finite sample grid only, not uniform C2 convergence.','Planar rr uses h=1e-4 profile finite differences.','Same physical g and same actual H function; spectral truncations differ explicitly.','No infinite-tail or nonlinear seam certificate.'],samples=len(records[0]['samples']),angles=len(records[0]['samples'][0]['jets']),records=[{k:d[k]for k in ['M','maxMetric','maxTensor','maxCurvature','whereTensor','_file','_sha']}for d in records],comparisons=rows);a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
