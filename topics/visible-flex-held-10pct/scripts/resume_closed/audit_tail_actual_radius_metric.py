#!/usr/bin/env python3
"""Metric of the explicit finite C2 tail at its actual radial coordinate.

All Fourier modes in the first-derivative Gram matrix are retained in the DFT
(the stated degree gate excludes aliasing). Radial sampling, floating Fourier
arithmetic and approximate background inversion remain numerical evidence.
The unchanged background is evaluated at R, while the perturbation uses the
literal one-ulp outer-cut lift. The caps carry their own fixed metric.
"""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
import argparse,hashlib,importlib.util,json,subprocess,sys,time
import numpy as np
p=argparse.ArgumentParser(description=__doc__)
for name in ['manifest','tail-reader','source-topic','checkpoint','out']:p.add_argument('--'+name,type=Path,required=True)
p.add_argument('--angular',type=int,default=512);p.add_argument('--fractions',default='0,.25,.5,.75');p.add_argument('--batch',type=int,default=128)
a=p.parse_args();started=time.monotonic()
spec=importlib.util.spec_from_file_location('actual_tail_reader',a.tail_reader);reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader);f=reader.IntegratedTail(a.manifest)
meta=f.meta;cut=np.longdouble(meta['parameters']['rCut']);c=np.longdouble(meta['radialGeometry']['outerAnchor']);width=np.longdouble('.02')
# The finite-data anchors and normalized increments define the exact model.
# Use span-local evaluation, avoiding cancellation in thin radial spans.
fractions=np.array([float(x)for x in a.fractions.split(',')],dtype=np.longdouble)
assert np.all((fractions>=0)&(fractions<1))
span=np.repeat(np.arange(len(f.L)),len(fractions));tt=np.tile(fractions,len(f.L))
rv=f.r[span]+f.L[span]*tt
# Invert the one-ulp quintic radius lift by its contraction fixed point.
R=rv.copy()
for _ in range(4):
 u=np.clip((R-(cut-width))/width,0,1);S=u**3*(10+u*(-15+6*u));R=rv-(c-cut)*S
max_inverse_lift=float(np.max(abs((R+(c-cut)*np.clip((R-(cut-width))/width,0,1)**3*(10+np.clip((R-(cut-width))/width,0,1)*(-15+6*np.clip((R-(cut-width))/width,0,1))))-rv)))
degree=int(2*max(max(abs(f.planar_modes-1)),max(f.height_modes)))
assert a.angular>2*degree
ang=np.arange(a.angular)*2*np.pi/a.angular;pm=f.planar_modes;hm=f.height_modes
planar=np.exp(1j*pm[:,None]*ang);height=np.cos(hm[:,None]*ang);height_t=-hm[:,None]*np.sin(hm[:,None]*ang)
co=np.cos(ang)[None,:];si=np.sin(ang)[None,:]
server=Path(__file__).with_name('background_metric_query.mjs')
proc=subprocess.Popen(['node',str(server),str(a.source_topic),str(a.checkpoint)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
info=json.loads(proc.stdout.readline());assert info.get('ready'),info
maximum=0.;l1maximum=0.;worst=None;inverse_max=0.;bg_iterations=0
try:
 for first in range(0,len(R),a.batch):
  sl=slice(first,first+a.batch);rr=R[sl];proc.stdin.write(json.dumps({'radii':[float(x)for x in rr]})+'\n');proc.stdin.flush()
  bg=json.loads(proc.stdout.readline())
  if 'error'in bg:raise RuntimeError(bg['error'])
  inverse_max=max(inverse_max,bg['maxInverseRadiusResidual']);bg_iterations=max(bg_iterations,bg['maxIterations'])
  w=np.array([x['w']for x in bg['rows']])[:,None];E=1+w*w
  vals=f.span_coefficients(span[sl],tt[sl]);V=np.asarray(vals[0],float);Vr=np.asarray(vals[1],float)
  u=np.clip((rr-(cut-width))/width,0,1);r1=1+(c-cut)*30*u*u*(1-u)**2/width
  Vr*=np.asarray(r1,float)[:,None]
  zR=Vr[:,f.P:]@height;zT=V[:,f.P:]@height_t
  xyR=Vr[:,:f.P]@planar;xyT=(V[:,:f.P]*(1j*pm))@planar
  r=np.asarray(rr,float)[:,None]
  er=(2*(co*xyR.real+si*xyR.imag)+abs(xyR)**2+2*w*zR+zR*zR)/E
  ef=(co*xyT.real+si*xyT.imag+r*(-si*xyR.real+co*xyR.imag)+np.real(xyR*np.conj(xyT))+(w+zR)*zT)/(r*np.sqrt(E))
  eg=(2*r*(-si*xyT.real+co*xyT.imag)+abs(xyT)**2+zT*zT)/(r*r)
  op=(abs(er+eg)+np.hypot(er-eg,2*ef))/2
  coeff=np.fft.fft(np.stack([er,ef,eg],axis=-1),axis=1)/a.angular
  norms=np.sum(abs(coeff),axis=1);l1=np.maximum(norms[:,0]+norms[:,1],norms[:,2]+norms[:,1])
  i,j=np.unravel_index(np.argmax(op),op.shape)
  if float(op[i,j])>maximum:
   maximum=float(op[i,j]);worst={'radius':float(rr[i]),'span':int(span[first+i]),'fraction':float(tt[first+i]),'theta':float(ang[j]),'background':bg['rows'][i]}
  l1maximum=max(l1maximum,float(l1.max()))
  if first%(a.batch*20)==0:print(json.dumps({'done':first+len(rr),'total':len(R),'metric':maximum,'fourier_l1_row':l1maximum}),flush=True)
finally:
 proc.stdin.close();proc.wait(timeout=20)
record=dict(scope=__doc__,command=sys.argv,source_sha256={x.name:hashlib.sha256(x.read_bytes()).hexdigest()for x in [Path(__file__),server]},inputs={str(x.resolve()):hashlib.sha256(x.read_bytes()).hexdigest()for x in [a.manifest,a.tail_reader,a.checkpoint]},
 finite_spans=len(f.L),radial_samples=len(R),fractions=[float(x)for x in fractions],angular_nodes=a.angular,exact_gram_fourier_degree=degree,alias_free_degree_gate=a.angular>2*degree,
 sampled_relative_operator_norm=maximum,sampled_radial_fourier_l1_row_norm=l1maximum,worst=worst,
 background_query=info,max_background_inverse_radius_residual=inverse_max,max_background_newton_iterations=bg_iterations,max_outer_lift_inverse_numerical_residual=max_inverse_lift,
 uniform_phase_reason='The material phase shift permutes the full angular domain and ambient rotations preserve the relative metric norm. Fixed caps use their own unchanged induced metric.',
 continuous_radial_certificate=False,interval_fourier_certificate=False,whole_exact_isometry_claimed=False,seconds=time.monotonic()-started)
a.out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:record[k]for k in ['sampled_relative_operator_norm','sampled_radial_fourier_l1_row_norm','worst','seconds']}))
