"""Run unchanged curve BVP with independently checked sparse exact-core evaluation.
Astra curve_transition, AI-assisted 2026-11-08. The profile, boundary equations,
core geometry, angular/radial audit and tolerances are unchanged. Only repeated
zero-term trig evaluation and unused high jets in perimeter integration are
removed. Use: python f6curve_sparse_run.py finite|bridge [the usual arguments].
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from f6direct_sparse_core import SparseReflectedCore,normalized_parameters

def sparse_parameters(self,p):
    model=SimpleNamespace(h0=self.h0,q=self.q,m=self.even,base_mode=self.base_mode,pscale=self.pscale,S=SimpleNamespace(arc_nodes=self.arc_nodes))
    return normalized_parameters(model,p)

def sparse_initial(self,p):
    if self._cache is not None and np.array_equal(p,self._cache):return self._cached
    par=self.parameters(p);core=SparseReflectedCore(par['R'],par['radial'],par['height'],self.arc_nodes);nt=max(256,16*int(self.even[-1]));theta=2*np.pi*np.arange(nt)/nt;exact=core.evaluate(par['halfwidth'],theta)
    if np.min(exact['den'])<=0:raise FloatingPointError('Exact rectifying core loses regularity')
    B,_,_=self.basis(nt);C=self.project(exact['F'][None,:,:],B)[:,0];out=(C-self.base(np.array([0.]))[:,0])/self.q;self._cache=p.copy();self._cached=out;return out

def install_sparse(cls):
    cls.parameters=sparse_parameters;cls.initial=sparse_initial

def mark_output(entry):
    original=entry.save_checkpoint
    def save(path,out):
        out['core_evaluator']='Unchanged exact R21 core, evaluated by f6direct_sparse_core.SparseReflectedCore via f6curve_sparse_run.py; original Cartesian geometry remains in the audit.'
        return original(path,out)
    entry.save_checkpoint=save

def check():
    from curve_stable_prefix_bvp import load_checkpoint
    from f6curve_outward_bvp import OutwardPrefix
    root=Path(__file__).parent.parent;path=root/'notes/f6curve_outward_base6_m24_q0075_local.json.gz';d=load_checkpoint(path);c=d['config'];o=OutwardPrefix(c['modes'],c['amplitude'],c['delta'],c['v_up'],c['v_down'],c['ramp'],c['cycles'],c['angular'],c['base_mode'],False);o.h0=d['h0'];p=np.asarray(d['parameters'])
    t=time.monotonic();old_par=o.parameters(p);old=o.initial(p);old_time=time.monotonic()-t
    install_sparse(OutwardPrefix);o._cache=None;t=time.monotonic();new_par=o.parameters(p);new=o.initial(p);new_time=time.monotonic()-t
    row=dict(scope='Independent original vs sparse exact-core normalization and coordinate projection at the frozen M24/q=.0075 parameters. Numerical equivalence check.',input=str(path),radius_difference=new_par['R']-old_par['R'],normalized_initial_max_difference=float(abs(new-old).max()),physical_initial_max_difference=float(o.q*abs(new-old).max()),old_seconds=old_time,new_seconds=new_time)
    (root/'notes/f6curve_sparse_core_check.json').write_text(json.dumps(row,indent=2)+'\n');print(json.dumps(row,indent=2))

if __name__=='__main__':
    mode=sys.argv.pop(1) if len(sys.argv)>1 else 'check'
    if mode=='check':check()
    elif mode=='finite':
        import f6curve_outward_bvp as entry
        install_sparse(entry.OutwardPrefix);mark_output(entry);entry.main()
    elif mode=='bridge':
        import f6curve_outward_bridge_bvp as entry
        install_sparse(entry.OutwardTailBVP);mark_output(entry);entry.main()
    else:raise SystemExit('Expected finite, bridge, or check')
