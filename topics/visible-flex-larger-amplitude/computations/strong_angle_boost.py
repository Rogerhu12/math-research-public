#!/usr/bin/env python3
"""Optional C2 angle-speed boost for the finite-neck provider.

The physical design field boost_law='angle' changes the old cubic radial-speed
boost to a C2 flat-top angular-speed turn with exactly the same endpoint
speeds and physical length. Other pieces are unchanged. It is a new metric.
The helper is inert for every existing profile without this field.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
P=Path(__file__).resolve().parent

def install(provider):
    if getattr(provider,'_strong_angle_boost_installed',False):return
    old_velocity=provider.velocity;old_jet=provider.piece_jet;old_prefix=provider.NeckPrefix
    def velocity(seg,u):
        if seg.get('strong_angle_boost'):
            return np.sin(provider.fl.phase(seg,u))
        return old_velocity(seg,u)
    def piece_jet(seg,u):
        if seg.get('strong_angle_boost'):
            u=np.asarray(u);phi=provider.fl.phase(seg,u)
            rate=np.sign(seg['p1']-seg['p0'])*seg['K']*provider.fl.ramp(u,seg['turn_ramp'])[0]
            return seg['a0']+seg['length']*provider.fl.integral(seg,u),np.sin(phi),np.cos(phi)*rate
        return old_jet(seg,u)
    class AngleBoostPrefix(old_prefix):
        def append(self,seg):
            if seg['kind']=='boost' and self.cfg.get('boost_law','cubic')=='angle':
                eps=.08;p0=math.asin(seg['v0']);p1=math.asin(seg['v1']);length=seg['length']
                if abs(p1-p0)<1e-14:raise ValueError('Angle boost must have unequal endpoint speeds')
                turn=provider.fl.turn(p0,p1,abs(p1-p0)/(length*(1-eps)))
                turn.update(kind='boost',v0=seg['v0'],v1=seg['v1'],strong_angle_boost=True)
                if abs(turn['length']-length)>2e-14:raise AssertionError('Physical boost length changed')
                seg=turn
            return super().append(seg)
        def breaks(self):
            # Interior ramp joins are C3 for a(s). Keeping the old knot topology
            # permits the explicit matched-knot design warm map; solve_bvp can
            # refine through these smooth internal points independently.
            out=[0.,self.end]
            for seg in self.segments:
                out.extend([seg['s0'],seg['s1']])
                if 'turn_ramp' in seg and not seg.get('strong_angle_boost'):
                    out.extend([seg['s0']+seg['length']*seg['turn_ramp'],seg['s0']+seg['length']*(1-seg['turn_ramp'])])
            return np.unique(out)
    provider.velocity=velocity;provider.piece_jet=piece_jet;provider.NeckPrefix=AngleBoostPrefix
    provider._strong_angle_boost_installed=True

def install_globals(namespace):
    """Apply the hook even to providers loaded without a sys.modules entry."""
    from types import SimpleNamespace
    proxy=SimpleNamespace(**namespace)
    install(proxy)
    for key in ('velocity','piece_jet','NeckPrefix','_strong_angle_boost_installed'):
        namespace[key]=getattr(proxy,key)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('profile','port','out','profile-out'):p.add_argument('--'+n,type=Path,required=True)
    a=p.parse_args();start=time.time()
    spec=importlib.util.spec_from_file_location('strong_angle_provider',P/'alternative-neck-provider.py')
    neck=importlib.util.module_from_spec(spec);spec.loader.exec_module(neck);install(neck)
    cfg=json.loads(a.profile.read_text());cfg['boost_law']='angle';port=json.loads(a.port.read_text());calls=[]
    def evaluate(x,details=False):
        c={**cfg,'delta':float(x[0]),'boost_length':float(x[1])}
        out=neck.LinearScreen(port,c).evaluate([x[0],c['vd']],details)
        if not details:calls.append(dict(delta=float(x[0]),boost_length=float(x[1]),residual=out.tolist()))
        return out
    seed=[cfg['delta'],cfg['boost_length']]
    z=least_squares(evaluate,seed,bounds=([.025,.04],[.3,.5]),x_scale=[.05,.1],xtol=3e-10,ftol=3e-10,gtol=3e-10,max_nfev=65)
    row=evaluate(z.x,True)
    result=dict(scope=__doc__,changed_metric_design=True,solver_success=bool(z.success),message=z.message,nfev=int(z.nfev),row=row,calls=calls,seconds=time.time()-start,source_sha256={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ('strong_angle_boost.py','alternative-neck-provider.py','alternative-neck-flatturn.py')},input_sha256=hashlib.sha256(a.profile.read_bytes()).hexdigest())
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    if row['residual_max']<2e-6:a.profile_out.write_text(json.dumps(row['profile'],indent=2)+'\n')
    print(json.dumps(dict(seconds=result['seconds'],nfev=z.nfev,profile=row['profile'],height=row['total_background_height'],residual=row['residual'],prefix=row['prefix']['background_kappa_sample'])),flush=True)
if __name__=='__main__':main()
