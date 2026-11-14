#!/usr/bin/env python3
"""Linear screen for a smooth, asymmetric first descending turn.

A positive descending_turn_bias slows the initial part of that turn and
speeds its last part while preserving total turning angle and physical
length. Its rate is K*ramp(u)*(1+bias*(2*u-1)). This is a new metric design,
not an isometric deformation or a solved nonlinear prefix.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
P=Path(__file__).resolve().parent

def weighted_integral(u,eps):
    """Exact polynomial integral of (2*v-1)*ramp(v) on [0,u]."""
    u=np.asarray(u)
    def left(t):
        t=np.clip(t/eps,0.,1.)
        return eps*(-t**3+(.5+1.5*eps)*t**4-.8*eps*t**5)
    middle=left(eps)+u*u-u-(eps*eps-eps)
    return np.where(u<eps,left(u),np.where(u>1-eps,left(1-u),middle))

def install(provider):
    if getattr(provider,'_strong_turn_bias_installed',False):return
    old_velocity=provider.velocity;old_jet=provider.piece_jet;old_prefix=provider.NeckPrefix
    def phase(seg,u):
        w,I=provider.fl.ramp(u,seg['turn_ramp'])
        return seg['p0']+(seg['p1']-seg['p0'])*(I+seg['strong_turn_bias']*weighted_integral(u,seg['turn_ramp']))/(1-seg['turn_ramp'])
    def integral(seg,u,which='sin'):
        u=np.asarray(u);out=np.zeros_like(u,dtype=float);fn=np.sin if which=='sin' else np.cos
        eps=seg['turn_ramp']
        for lo,hi in zip((0.,eps,1-eps),(eps,1-eps,1.)):
            width=np.clip(u-lo,0,hi-lo);v=lo+width[...,None]*provider.base.gu
            out+=width/2*(fn(phase(seg,v))@provider.base.gw)
        return out
    def velocity(seg,u):
        if 'strong_turn_bias' in seg:return np.sin(phase(seg,u))
        return old_velocity(seg,u)
    def piece_jet(seg,u):
        if 'strong_turn_bias' in seg:
            u=np.asarray(u);phi=phase(seg,u)
            rate=np.sign(seg['p1']-seg['p0'])*seg['K']*provider.fl.ramp(u,seg['turn_ramp'])[0]*(1+seg['strong_turn_bias']*(2*u-1))
            return seg['a0']+seg['length']*integral(seg,u),np.sin(phi),np.cos(phi)*rate
        return old_jet(seg,u)
    class BiasedPrefix(old_prefix):
        def append(self,seg):
            bias=float(self.cfg.get('descending_turn_bias',0.))
            if abs(bias)>=1:raise ValueError('Turn speed must remain of one sign')
            if bias and seg['kind']=='turn' and seg['p0']>0>seg['p1'] and not hasattr(self,'loop_begin'):
                seg=dict(seg,strong_turn_bias=bias)
                seg['dr']=seg['length']*float(integral(seg,1.))
                seg['dh']=seg['length']*float(integral(seg,1.,'cos'))
                rr=seg['length']*integral(seg,np.linspace(0,1,301));seg['dr_min']=float(rr.min());seg['dr_max']=float(rr.max())
            return super().append(seg)
    provider.velocity=velocity;provider.piece_jet=piece_jet;provider.NeckPrefix=BiasedPrefix
    provider._strong_turn_bias_installed=True

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('profile','port','out','profile-out'):p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--bias',type=float,default=.3);p.add_argument('--turn-curvature',type=float,default=5.7)
    a=p.parse_args();start=time.time();source_hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ('strong_turn_bias.py','strong_angle_boost.py','alternative-neck-provider.py')}
    spec=importlib.util.spec_from_file_location('strong_bias_provider',P/'alternative-neck-provider.py');neck=importlib.util.module_from_spec(spec);spec.loader.exec_module(neck);install(neck)
    cfg=json.loads(a.profile.read_text());cfg['descending_turn_bias']=a.bias;cfg['descending_turn_curvature']=a.turn_curvature;port=json.loads(a.port.read_text());calls=[]
    def evaluate(x,details=False):
        c={**cfg,'delta':float(x[0]),'boost_length':float(x[1])}
        out=neck.LinearScreen(port,c).evaluate([x[0],c['vd']],details)
        if not details:calls.append(dict(x=[float(v) for v in x],residual=out.tolist()))
        return out
    seed=[cfg['delta'],cfg['boost_length']]
    z=least_squares(evaluate,seed,bounds=([.025,.04],[.3,.5]),x_scale=[.05,.1],xtol=3e-10,ftol=3e-10,gtol=3e-10,max_nfev=65)
    row=evaluate(z.x,True)
    result=dict(scope=__doc__,changed_metric_design=True,solver_success=bool(z.success),message=z.message,nfev=int(z.nfev),row=row,calls=calls,seconds=time.time()-start,source_sha256=source_hashes)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    if row['residual_max']<2e-6:a.profile_out.write_text(json.dumps(row['profile'],indent=2)+'\n')
    print(json.dumps(dict(seconds=result['seconds'],nfev=z.nfev,profile=row['profile'],height=row['total_background_height'],residual=row['residual'],prefix=row['prefix']['background_kappa_sample'])),flush=True)
if __name__=='__main__':main()
