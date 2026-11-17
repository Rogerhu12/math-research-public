#!/usr/bin/env python3
"""Run immutable numerical-m2-prefix.py with a two-checkpoint secant initial guess.
Only source initial-guess selection changes; original BVP residuals and audit stay.
Pass --numerical-script and all ordinary prefix arguments plus --restart-second.
No generated source copy is written to the repository or persisted by this tool.
"""
import argparse,hashlib,sys
from pathlib import Path
p=argparse.ArgumentParser(add_help=False,allow_abbrev=False);p.add_argument('--numerical-script',type=Path,required=True);a,remaining=p.parse_known_args();source=a.numerical_script.read_text();digest=hashlib.sha256(source.encode()).hexdigest()
EXPECTED='d9f8e1f6707bfb058a763fd7c0638543b9843d54e78ca419fc7d2cc24c9e4360'
if digest!=EXPECTED:raise SystemExit('Unexpected source version: '+digest)
HELPER='def secant_restart(obj,a):\n    """Initial-guess predictor only; equations, physical port and audit unchanged."""\n    from curve_stable_prefix_bvp import load_checkpoint\n    if a.fixed:raise ValueError(\'Secant predictor is for metric design only; use the original fixed refinement.\')\n    old=load_checkpoint(a.restart);previous=load_checkpoint(a.restart_second)\n    if not old.get(\'solver_success\')or not previous.get(\'solver_success\'):raise ValueError(\'Secant predictor requires two successful checkpoints\')\n    qo=old[\'actual_primary_amplitude\'];qp=previous[\'actual_primary_amplitude\']\n    if not qp<qo<a.amplitude:raise ValueError(\'Secant continuation requires previous q < recent q < target q\')\n    x,y,par=obj.restart(a.restart);xp,yp,pp=obj.restart(a.restart_second)\n    if x.shape!=xp.shape or float(abs(x-xp).max())>1e-13:raise ValueError(\'Restart meshes differ\')\n    t=(a.amplitude-qo)/(qo-qp);y=y+t*(y-yp);par=par+t*(par-pp)\n    f=obj.flow(par[0]);s,_=obj.chart(x,par[0]);correction=obj.initial(par)-y[:,0];cutoff=(f.Tu if f.direction==\'outward\'else f.Td)/2;y+=correction[:,None]*np.maximum(0,1-s/cutoff)[None,:]**3\n    print(json.dumps(dict(event=\'secant_predictor\',previous_q=qp,recent_q=qo,target_q=a.amplitude,weight=t,delta=obj.cfg[\'delta\']+par[0])),flush=True)\n    return x,y,par\n\n'

old='if a.restart:x,y,par=obj.restart(a.restart)';new='if a.restart_second:x,y,par=secant_restart(obj,a)\n        elif a.restart:x,y,par=obj.restart(a.restart)'
if source.count(old)!=1 or source.count('def run(a):')!=1:raise SystemExit('Source anchor mismatch')
source=source.replace('def run(a):',HELPER+'def run(a):').replace(old,new).replace("p.add_argument('--restart',type=Path);", "p.add_argument('--restart-second',type=Path);p.add_argument('--restart',type=Path);")
meta={'original_sha256':digest,'launcher_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Two verified successful checkpoints predict only an initial guess; residuals, physical port and audit unchanged.'}
source=source.replace('TRANSFORMS={}',"TRANSFORMS={'entry_secant_predictor':"+repr(meta)+"}")
sys.argv=[str(a.numerical_script),*remaining]
exec(compile(source,str(a.numerical_script),'exec'),{'__name__':'__main__','__file__':str(a.numerical_script)})
