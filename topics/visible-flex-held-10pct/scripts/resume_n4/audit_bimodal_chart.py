#!/usr/bin/env python3
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np,json,sys,hashlib
from pathlib import Path
from bimodal_chart_loader import load,module
source=Path('bundle/topics/visible-flexible-closed-surface').resolve();eta=.3674128048915633
sys.path[:0]=[str(source/'notes'),str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
ad=load(source,4,eta);module('chart_audit_bridge',source.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py').install()
Flow,_=ad.build_classes(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.))
cfg=json.loads(Path('vu035-profile.json').read_text());port=json.loads(Path('mode4_port24.json').read_text());port['cut']['_prefix_bridge']=cfg['prefix_bridge']
f=Flow(cfg,port,8,.06,512,4,warp_q=.06)
s=f.end*np.array([.013,.19,.41,.63,.79,.86,.94]);g=f.geo(s,512);h=1e-6
P=f.geo(s+h,512);Q=f.geo(s-h,512)
num=(P['pos']-Q['pos'])/(2*h)
num2=(P['s1']-Q['s1'])/(2*h)
freq=np.fft.fftfreq(512,1/512)
fp=np.fft.ifft(np.fft.fft(g['pos'],axis=1)*(1j*freq)[None,:,None],axis=1).real
fpp=np.fft.ifft(np.fft.fft(g['pos'],axis=1)*(-freq**2)[None,:,None],axis=1).real
ang=f.angular(512);inlet=f.geo(np.array([0.]),512);cut=f.geo(np.array([f.end]),512)
out=dict(scope='Finite numerical check of exact coordinate formulas; no physical BVP conclusion',eta=eta,q=.06,radial_first_difference_error=float(abs(num-g['s1']).max()),radial_second_difference_error=float(abs(num2-g['s2']).max()),angular_first_fft_error=float(abs(fp-g['p1']).max()),angular_second_fft_error=float(abs(fpp-g['p2']).max()),inlet_angle_error=float(abs(ang[1]-inlet['theta'][0]).max()),cut_chart_error=max(float(abs(cut[k]).max())for k in ('v','vs','vp','e')),chart_rho_min=float(g['rho'].min()),global_chart_rho_lower=1-.9*(eta+(1+eta)**2/(8*eta)),source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in (Path('bimodal_chart_loader.py'),Path(__file__))})
Path('bimodal-chart-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
