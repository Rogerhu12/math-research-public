#!/usr/bin/env python3
"""Fixed future inward reference tail; no nonaxisymmetric cut is extrapolated."""
import argparse,gzip,hashlib,json,subprocess
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicHermiteSpline
import parallel_20261117_inward_profile as profile
import parallel_20261117_dynamic_tail as dynamic

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
p=argparse.ArgumentParser(description=__doc__)
for k in ('parent','primitive-background','source','out'):p.add_argument('--'+k,type=Path,required=True)
a=p.parse_args();d=json.loads(gzip.decompress(a.parent.read_bytes()))
if not d['success']or sha(profile.__file__)!=d['inward_profile_sha256']:raise ValueError('Parent/profile identity')
z=d['inward_scalar_profile'];g=profile.InwardProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'],z['cut'],z['curvature'],z['ramp_in'],z['ramp_out'],z['quadrature'])
s=g.cut+g.ramp_in+(g.alpha1-np.arcsin(-.8))/g.curvature;r,ap,app=g(s);hs=np.sqrt(1-ap*ap);w=-hs/ap;wr=app/(ap**3*hs)
if not(g.alpha2<np.arcsin(-.8)<g.alpha1):raise ValueError('Port outside constant curvature segment')
old=json.loads(a.primitive_background.read_bytes())['parameters'];drop={'spacing','rCuff','oldCut','epsilonScale','prefixRByCell','constructor'}
cfg={k:v for k,v in old.items()if k not in drop};cfg.update(rCut=r-.01,wCut=w,width=r-.01-g.radius,curvatureBound=5.,orientation=1,prefixR=64.,valleyControls=[0.]*len(old['valleyControls']),pulseCaps=[[.4,.1]])
c=a.out.with_suffix('.config.json');n=a.out.with_suffix('.native.json');c.write_text(json.dumps(dict(parameters=cfg),indent=2)+'\n')
exporter=Path(dynamic.__file__).with_name('parallel_20261117_tail_background.mjs')
with a.out.with_suffix('.native.log').open('w')as f:
 subprocess.run(['node',str(exporter),'--source',str(a.source),'--config',str(c),'--depth','4','--steps','64','--modes','8','--out',str(n)],stdout=f,stderr=subprocess.STDOUT,check=True)
b=json.loads(n.read_bytes());end=b['rows'][-1];r0=end['r'];bridge=CubicHermiteSpline([r0,r],[end['logw'],np.log(w)],[end['dlogwdr'],wr/w])
for j in range(1,65):
 rr=r0+(r-r0)*j/64;b['rows'].append(dict(r=rr,logw=float(bridge(rr)),dlogwdr=float(bridge(rr,1)),cell=-1,segment=0,x=j/64))
port=dict(s=s,r=r,a_prime=ap,a_second=app,height_s=hs,w=w,w_r=wr)
b.update(scope=__doc__,source_sha256=sha(__file__),parent_sha256=sha(a.parent),inward_profile_sha256=sha(profile.__file__),primitive_background_sha256=sha(a.primitive_background),native_exporter_sha256=sha(exporter),native_output_sha256=sha(n),actual_parent_end=d['mesh'][-1],actual_nonaxisymmetric_cut_available=False,reference_port=port,shallow_at='right',deep_at='left',cut=dict(r=r,w=w,w_r=wr),bridge=dict(r0=r0,r1=r,width=r-r0),target_cuff_radius=g.radius,angular_trace=None)
a.out.write_text(json.dumps(b)+'\n');bg=dynamic.Background(a.out,'physical-r');audit={}
for order in (8,16):
 t,v=np.polynomial.legendre.leggauss(order);h=np.diff(bg.r);rr=bg.r[:-1,None]+h[:,None]*(t+1)/2;ww=np.exp(bg.spline(rr));E=1+ww*ww
 audit[order]=dict(height=float(np.sum(h*(ww@v)/2)),length=float(np.sum(h*(np.sqrt(E)@v)/2)),sampled_curvature=float(np.max(abs(ww*bg.spline(rr,1))/E**1.5)))
report=dict(background_sha256=sha(a.out),reference_port=port,old_remaining_arclength=g.end-s,old_remaining_height=g.shift3[1]-g.meridian(s)['height_increment'],finite_intervals=len(bg.r)-1,audit=audit)
a.out.with_suffix('.report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
