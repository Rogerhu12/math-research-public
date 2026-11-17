#!/usr/bin/env python3
"""Portable small-cut finite-linear-port prefix design and continuation.

Run recover_prefix.py first into --recovery. This script restores three extra
immutable source/port files from the adjacent manifest patch, constructs a fresh
linear f/a chart for the requested bridge/profile, and solves increasing q.
No generated checkpoint is a closed isometric surface. Logs, data and small
summary are written only to --output. No repository mutation is performed.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,math,subprocess,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from scipy.interpolate import PPoly

def restore_extra(repo,recovery,patch):
 d=json.loads(patch.read_text());out=[]
 for r in d['files']:
  dest=recovery/r['target']
  if dest.is_file():data=dest.read_bytes()
  else:
   data=subprocess.check_output(['git','-C',str(repo),'show',r['revision']+':'+r['path']]);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
  if len(data)!=r['bytes'] or hashlib.sha256(data).hexdigest()!=r['sha256']:raise RuntimeError('Source checksum mismatch: '+str(dest))
  out.append(r)
 return out

def prepare(source,comp,port,cfg,out):
 spec=importlib.util.spec_from_file_location('smallcut_numerical',comp/'numerical-m2-prefix.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 ad=mod.load(source);short=mod.source_module('smallcut_bridge',comp/'root_short_bridge.py');short.install()
 port=json.loads(port.read_text());port['cut']['_prefix_bridge']=cfg['prefix_bridge'];Flow,BVP=ad.build_classes({'knots':[0.,1.],'values':[1.,1.],'final_derivative':0.})
 def make(d):return Flow({**cfg,'delta':float(d)},port,4,.02,128,2)
 cache={}
 def target(d):
  d=float(d)
  if d not in cache:cache[d]=float(make(d).backward_line().core[1])
  return cache[d]
 lo=max(.003,cfg['delta']*.65);hi=min(.8,cfg['delta']*1.4)
 if target(lo)*target(hi)>0:
  vals=[(float(x),target(x))for x in np.geomspace(.005,.8,30)];br=[(x0,x1)for (x0,y0),(x1,y1)in zip(vals,vals[1:])if y0*y1<0]
  if not br:raise RuntimeError('No linear mode-two branch root in [.005,.8]')
  lo,hi=min(br,key=lambda z:abs((z[0]+z[1])/2-cfg['delta']))
 delta=brentq(target,lo,hi,xtol=2e-12);cfg={**cfg,'delta':float(delta)};f=make(delta);line=f.backward_line();x=np.linspace(0,1,65);s=x*f.end;fg=np.empty((2,len(s)))
 for j,(lo,hi,sol,scale)in enumerate(line.segments):
  mask=(s>=lo)&((s<hi)if j+1<len(line.segments)else(s<=hi))
  if np.any(mask):fg[:,mask]=sol(s[mask])*math.exp(scale-line.logscale)/line.core[0]
 ar,ap,_=f.profile(s);h=fg[0]/ar;rhs=f.linear_rhs(f.end,fg[:,-1]);hp=(rhs[0]*ar[-1]-fg[0,-1]*ap[-1])/ar[-1]**2*f.end
 chart=dict(scope='Normalized linear mode-two f/a followed by quintic end cutoff; numerical angular coordinate only.',reference_profile=cfg,knots=x.tolist(),values=h.tolist(),final_derivative=float(hp))
 (out/'profile.json').write_text(json.dumps(cfg,indent=2)+'\n');(out/'chart.json').write_text(json.dumps(chart,indent=2)+'\n')
 # The second stable line is diagnostic only: zero would be a core resonance,
 # not a zero terminal height of a nonzero solution.
 l2=f.backward_line(1)
 linear=dict(profile=cfg,bridge=f.bridge.summary(),meridian_length=f.end,first_terminal_fg_per_unit_core=fg[:,-1].tolist(),second_mode_core_transversality=float(l2.core[1]),chart_range=[float(h.min()),float(h.max())],root_samples=sorted(cache.items()))
 ss=np.unique(np.r_[np.linspace(0,f.end,2049),f.breaks]);aa,vv,acc=f.profile(ss);bb=np.sqrt(1-vv*vv)
 linear['sampled_background']=dict(height=float(np.trapezoid(bb,ss)),meridian_curvature=float(np.max(np.abs(acc)/bb)),parallel_curvature=float(np.max(bb/aa)),radius_max=float(np.max(aa)))
 (out/'linear.json').write_text(json.dumps(linear,indent=2)+'\n');print(json.dumps(dict(event='linear',delta=delta,H1_per_q=float(fg[1,-1]),bridge_height=linear['bridge']['height'],bridge_minimum_cosine=linear['bridge']['minimum_cosine'],mode4_transversality=linear['second_mode_core_transversality'])),flush=True)
 return linear

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--repo',type=Path,required=True);p.add_argument('--recovery',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--patch',type=Path,default=Path(__file__).with_name('smallcut_manifest_patch.json'))
 p.add_argument('--radius',choices=['.30','.35'],default='.35');p.add_argument('--port',type=Path);p.add_argument('--curvature',type=float,default=4.);p.add_argument('--peak-fraction',type=float,default=.5);p.add_argument('--vu',type=float,default=.55);p.add_argument('--vd',type=float,default=.6);p.add_argument('--delta-guess',type=float,default=.1718)
 p.add_argument('--cycles',type=int,default=1);p.add_argument('--stages',default='.02:8,.04:8,.06:8,.08:10,.10:10,.12:12,.14:12,.16:14,.18:16,.20:16');p.add_argument('--tol',type=float,default=1e-6);p.add_argument('--max-nodes',type=int,default=4000);p.add_argument('--stage-timeout',type=float,default=900);p.add_argument('--restart',type=Path);p.add_argument('--linear-only',action='store_true');a=p.parse_args()
 a.output.mkdir(parents=True,exist_ok=True);extra=restore_extra(a.repo,a.recovery,a.patch)
 source=a.recovery/'bundle/topics/visible-flexible-closed-surface';comp=a.recovery/'bundle/topics/visible-flex-larger-amplitude/computations'
 port=a.port or comp/('numerical-m2-tail-smallcut-30-port32-r2048.json'if a.radius=='.30'else'numerical-m2-tail-smallcut-35-port16-r1024.json')
 cfg=dict(direction='outward',vu=a.vu,vd=a.vd,delta=a.delta_guess,ramp=.4,ramp_eta=.05,ramp_law='flat',cycles=a.cycles,prefix_bridge=dict(kind='turn_plateau_v1',curvature=a.curvature,peak_fraction=a.peak_fraction))
 linear=prepare(source,comp,port,cfg,a.output);records=[];restart=a.restart
 manifest=dict(scope=__doc__,extra_sources=extra,port_sha256=hashlib.sha256(port.read_bytes()).hexdigest(),parameters=vars(a).copy())
 manifest['parameters']={k:str(v)if isinstance(v,Path)else v for k,v in manifest['parameters'].items()};(a.output/'run_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 if a.linear_only:return
 for st in a.stages.split(','):
  qs,ms=st.split(':');q=float(qs);M=int(ms);name=f'q{round(q*1000):03d}-m{M}';out=a.output/name;log=out.with_suffix('.log')
  cmd=[sys.executable,'-u',str(comp/'numerical-m2-prefix.py'),'--source-topic',str(source),'--profile',str(a.output/'profile.json'),'--chart',str(a.output/'chart.json'),'--port',str(port),'--out-prefix',str(out),'--amplitude',str(q),'--warp-reference',str(q),'--modes',str(M),'--angular',str(max(256,32*M)),'--audit-angular',str(max(512,64*M)),'--nodes','401','--max-nodes',str(a.max_nodes),'--tol',str(a.tol),'--bc-tol','1e-7','--physical-bc-tol','2e-9']
  if restart:cmd+=['--restart',str(restart)]
  print(json.dumps(dict(event='stage_start',name=name)),flush=True);t=time.time();timeout=False
  with log.open('w')as f:
   try:ret=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=a.stage_timeout).returncode
   except subprocess.TimeoutExpired:ret=None;timeout=True
  summ=out.with_name(name+'-summary.json');d=json.loads(summ.read_text())if summ.is_file()else {'solver_success':False,'error':'Timed out'if timeout else'No summary; inspect log'}
  z=dict(name=name,command=cmd,elapsed=time.time()-t,returncode=ret,timeout=timeout,success=d.get('solver_success'),error=d.get('error'),nodes=d.get('nodes'),delta=d.get('frozen_profile',{}).get('delta'),max_rms=d.get('max_rms_collocation_residual'))
  z.update({k:v for k,v in d.get('summary',{}).items()if k in ['metric_l1','flow_defect','darboux_l1','kappa_sample','height_max','radius_max','root_min','terminal_height_coeff_max']})
  if z['success']:
   from curve_stable_prefix_bvp import load_checkpoint
   rec=load_checkpoint(out.with_suffix('.json.gz'));pp=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),np.asarray(rec['mesh']),extrapolate=True,axis=1);end=rec['meridian_length'];H=q*pp(end)[-M:];Hs=q*pp(end,1)[-M:];cut=rec['physical_tail_cut'];Hr=-math.sqrt(cut['E'])*Hs
   trace=dict(scope='Signed physical cosine height modes at identity angular cut. Finite-prefix trace only; mean and Cartesian nonlinear seam unpaid.',modes=(2*np.arange(1,M+1)).tolist(),H=H.tolist(),Hs=Hs.tolist(),Hr=Hr.tolist(),H_l1=float(np.abs(H).sum()),sigma=-1.,cut=cut,actual_primary_amplitude=rec['actual_primary_amplitude'])
   out.with_name(name+'-H.json').write_text(json.dumps(trace,indent=2)+'\n');z['H1']=float(H[0]);z['H2']=float(H[1]);z['H_l1']=trace['H_l1']
  records.append(z);(a.output/'continuation.json').write_text(json.dumps(records,indent=2)+'\n');print(json.dumps({k:v for k,v in z.items()if k!='command'}),flush=True)
  if not z['success']:break
  restart=out.with_suffix('.json.gz')
if __name__=='__main__':main()
