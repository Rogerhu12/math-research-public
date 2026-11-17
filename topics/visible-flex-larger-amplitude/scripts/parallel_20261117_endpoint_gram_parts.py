#!/usr/bin/env python3
"""Read-only endpoint Gram/omitted-spectrum decomposition at the field's saved N."""
import argparse,gzip,hashlib,json
from pathlib import Path
import numpy as np
from parallel_20261117_frenet_symbol import Frenet
import parallel_20261117_inward_profile as profile
p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();d=json.loads(gzip.decompress(a.input.read_bytes()))
if not d['success']or sha(profile.__file__)!=d['inward_profile_sha256']:raise ValueError('Accepted actual inward source required')
q=Frenet(d['M'],d['N']);z=d['inward_scalar_profile'];g=profile.InwardProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'],z['cut'],z['curvature'],z['ramp_in'],z['ramp_out'],z['quadrature'])
y=np.array(d['states'][-1]);ys=np.array(d['rhs'][-1]);r,ap,app=g(d['mesh'][-1]);k=ap/r
rho=1+np.cos(q.angle[:,None]*q.freq[None,1:])@((1-q.freq[1:]**2)*np.array(d['states'][0][1:q.M+1]));target=(r*rho)**2
F,t,e=q.jet(y);V,dV,_=q.jet(ys);raw=q.local(y,k)['V'];tail=raw-V;H=np.fft.rfft(raw,axis=0)
f=np.arange(len(H));first=(f>2*q.M)&(f<=4*q.M-6);rest=f>4*q.M-6
vfirst=np.fft.irfft(H*first[:,None],n=q.N,axis=0);vrest=np.fft.irfft(H*rest[:,None],n=q.N,axis=0)
def gram(v):
 er=np.sum(v*v,axis=1)-1;gr=np.sum(t*t,axis=1)/target-1;fr=np.sum(v*t,axis=1)/np.sqrt(target);op=(abs(er+gr)+np.sqrt((er-gr)**2+4*fr*fr))/2;j=int(np.argmax(op))
 return dict(max=float(op[j]),angle=float(q.angle[j]),at_max=dict(er=float(er[j]),gr=float(gr[j]),fr=float(fr[j])),component_max=dict(er=float(max(abs(er))),gr=float(max(abs(gr))),fr=float(max(abs(fr)))))
def norm(v):return float(np.max(np.linalg.norm(v,axis=1)))
coeff=2*H/q.N
rows=[]
for c,name in enumerate(('R','T','Z')):
 value=-coeff[:,c].imag if name=='T' else coeff[:,c].real
 def band(mask):
  ix=np.where(mask&(f%2==0))[0];j=ix[np.argmax(abs(value[ix]))];return dict(max=float(abs(value[j])),mode=float(j/2),signed=float(value[j]))
 rows.append(dict(component=name,first_omitted=band(first),beyond_221=band(rest)))
report=dict(scope=__doc__,input_sha256=sha(a.input),source_sha256=sha(__file__),M=q.M,N=q.N,end=d['mesh'][-1],
 actual_saved_rhs_gram=gram(V),raw_velocity_algebraic_gram=gram(raw),remove_first_band_algebraic_gram=gram(raw-vfirst),remove_later_band_algebraic_gram=gram(raw-vrest),
 tail_norm=norm(tail),first_band_norm=norm(vfirst),later_band_norm=norm(vrest),tail_reconstruction_gap=norm(tail-vfirst-vrest),spectrum=rows,
 angular_gram_rate_max=float(max(abs(2*np.sum(t*dV,axis=1)/target-2*k*np.sum(t*t,axis=1)/target))),
 saved_rhs_difference=float(max(abs(q.rhs(y,k)-ys))))
a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print('sha256',sha(a.out))
