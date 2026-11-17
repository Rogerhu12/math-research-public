#!/usr/bin/env python3
"""Run the original m3 BVP with optional two-state secant initialization.

The solver, residuals, core parameters and domain guard are unchanged. Domain
diagnostics record rejected trial positions. The optional secant changes only
the initial guess. A finite linear DN still gives only an OPEN prefix.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
import argparse,hashlib,importlib.util,json,sys,time,traceback

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
 p=argparse.ArgumentParser(add_help=False);p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--short-bridge',type=Path);p.add_argument('--secant-low',type=Path);p.add_argument('--diagnose-domain',action='store_true')
 a,rest=p.parse_known_args();record=dict(scope=__doc__,command=[sys.executable,*sys.argv],wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 runfile=None
 if '--out-prefix'in rest:
  out=Path(rest[rest.index('--out-prefix')+1]);runfile=out.with_name(out.name+'-run.json');runfile.write_text(json.dumps(record,indent=2)+'\n')
 src=a.source_topic.resolve();ad=module('m3_prefix_adaptive',src/'scripts/950f-prefix-adaptive-chart-bvp-v2.py');patch=module('m3_prefix_flat',src/'scripts/db6f-prefix-flat-profile.py');patch.install(ad)
 if a.short_bridge:
  short=module('m3_prefix_short',a.short_bridge.resolve());original=ad.old.install_source
  def install(root):original(root);short.install()
  ad.old.install_source=install
 if a.secant_low or a.diagnose_domain:
  import numpy as np
  base_build=ad.build_classes
  diagnostics=dict(calls=0,last=[])
  def build(chart):
   Flow,BVP=base_build(chart)
   if a.diagnose_domain:
    original_frame=Flow.frame
    def frame(self,s,C,B1=None,B2=None):
     try:return original_frame(self,s,C,B1,B2)
     except FloatingPointError:
      bb1=self.B1 if B1 is None else B1;bb2=self.B2 if B2 is None else B2
      g=self.geo(s,bb1.shape[1]);ar,ap,_=self.profile(s);d=self.values(C,bb1)+g['p1'];dd=self.values(C,bb2)+g['p2'];lam=np.sqrt(np.sum(d*d,axis=2));T=d/lam[:,:,None];normal=dd-np.sum(dd*T,axis=2)[:,:,None]*T;nn=np.sqrt(np.sum(normal*normal,axis=2));kap=nn/lam**2;alpha=-ap[:,None]/(ar[:,None]*kap);margin=(1-alpha**2).real;i,j=np.unravel_index(np.argmin(margin),margin.shape)
      diagnostics['calls']+=1;diagnostics['last'].append(dict(min_margin=float(margin[i,j]),s=float(np.asarray(s)[i]),s_over_end=float(np.asarray(s)[i]/self.end),psi=float(2*np.pi*j/bb1.shape[1]),radius=float(ar[i]),radius_s=float(ap[i]),curve_kappa=float(kap[i,j].real),min_speed=float(lam.real.min()),min_normal_acceleration=float(nn.real.min())))
      diagnostics['last']=diagnostics['last'][-12:]
      raise
    Flow.frame=frame
   if a.secant_low:
    original_restart=BVP.restart
    def restart(self,path):
     from curve_stable_prefix_bvp import load_checkpoint
     if self.fixed:raise ValueError('Secant design predictor is not a fixed-g refinement rule')
     hi=load_checkpoint(path);lo=load_checkpoint(a.secant_low);qh=hi['actual_primary_amplitude'];ql=lo['actual_primary_amplitude']
     if not 0<ql<qh<self.q:raise ValueError('Expected 0 < q_low < q_high < target q')
     th,yh,ph=original_restart(self,path);tl,yl,pl=original_restart(self,a.secant_low)
     if not np.array_equal(th,tl):raise ValueError('Secant target meshes differ')
     w=(self.q-qh)/(qh-ql);w2=(self.q**2-qh**2)/(qh**2-ql**2)
     y=yh+w*(yh-yl);par=ph+w2*(ph-pl)
     f=self.flow(par[0]);s,_=self.chart(th,par[0]);correction=self.initial(par)-y[:,0];cutoff=(f.Tu if f.direction=='outward'else f.Td)/2;y+=correction[:,None]*np.maximum(0,1-s/cutoff)[None,:]**3
     record['secant']=dict(high=str(path),low=str(a.secant_low),high_sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest(),low_sha256=hashlib.sha256(a.secant_low.read_bytes()).hexdigest(),high_q=qh,low_q=ql,target_q=self.q,normalized_shape_weight=w,even_design_parameter_weight=w2,inlet_correction_linf=float(abs(correction).max()))
     print(json.dumps(dict(event='secant_initialization',**record['secant'])),flush=True)
     return th,y,par
    BVP.restart=restart
   return Flow,BVP
  ad.build_classes=build
  record['domain_diagnostics']=diagnostics
 sys.argv=[sys.argv[0],'--source-root',str(src/'repro/source-root')]+rest
 t=time.time()
 try:
  ad.main();record['completed']=True
 except Exception as exc:
  traceback.print_exc()
  if '--out-prefix'in rest:
   out=Path(rest[rest.index('--out-prefix')+1]);out.with_name(out.name+'-failure.json').write_text(json.dumps(dict(scope=__doc__,error=repr(exc),seconds=time.time()-t,command=sys.argv),indent=2)+'\n')
  record.update(completed=False,error=repr(exc))
  raise
 finally:
  record['seconds']=time.time()-t
  if runfile:runfile.write_text(json.dumps(record,indent=2)+'\n')
if __name__=='__main__':main()
