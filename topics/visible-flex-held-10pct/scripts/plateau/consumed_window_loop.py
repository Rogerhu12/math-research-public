"""Loop extensions after the fixed held strip; exploratory metric designs.

Every polynomial knot is retained.  The original protected H strip and the
extra negative-K ramp are unchanged.  No nonlinear existence is asserted.
"""
from __future__ import annotations
import math
import numpy as np
from consumed_window_profile import ConsumedWindowProfile,turn


class ConsumedWindowLoop:
    def __init__(self,extra_speed=.38,extra_acceleration=1.,return_speed=.5,
                 turn_acceleration=5.5,stop_acceleration=5.5,
                 final_length=.65,stop_speed=0.,cut_radius=.6,cut_w=.5,
                 cut_wr=None,eta=.05):
        self.parameters=dict(extra_speed=extra_speed,
            extra_acceleration=extra_acceleration,return_speed=return_speed,
            turn_acceleration=turn_acceleration,stop_acceleration=stop_acceleration,
            final_length=final_length,stop_speed=stop_speed,cut_radius=cut_radius,
            cut_w=cut_w,cut_wr=cut_wr,eta=eta)
        self.head=ConsumedWindowProfile(extra_speed=extra_speed,
            extra_acceleration=extra_acceleration,eta=eta)
        self.delta=self.head.delta;self.Tu=self.head.Tu;self.eta=eta
        self.hold_end=self.head.hold_end;self.direction='outward'
        self.final_v=-1/math.sqrt(1+cut_w*cut_w)
        self.final_acc=-cut_w*(-7*cut_w/cut_radius if cut_wr is None else cut_wr)/(1+cut_w*cut_w)**2
        self.v1=extra_speed;self.v2=-return_speed;self.v3=stop_speed
        Lturn=(extra_speed+return_speed)/(turn_acceleration*(1-eta))
        Lstop=(return_speed+stop_speed)/(stop_acceleration*(1-eta))
        a_extra=self.head.a_extra
        self.a_turn=a_extra+Lturn*(extra_speed-return_speed)/2
        integral_final=final_length*(stop_speed+self.final_v)/2-.1*final_length**2*self.final_acc
        self.a_bridge=cut_radius-integral_final
        self.a_stop=self.a_bridge-Lstop*(stop_speed-return_speed)/2
        Lcoast=(self.a_turn-self.a_stop)/return_speed
        self.lengths=np.array([*self.head.lengths[:2],Lturn,Lcoast,Lstop,final_length])
        if min(self.lengths)<=0:raise ValueError('Negative coast or segment length')
        self.ends=np.r_[0.,np.cumsum(self.lengths)];self.end=float(self.ends[-1])
        self.prefix_end=float(self.ends[5]);self.a_extra=a_extra
        self.breaks=np.unique(np.r_[self.head.breaks[self.head.breaks<=self.head.ends[2]],
            self.ends,self.ends[2]+Lturn*np.array([eta,1-eta]),
            self.ends[4]+Lstop*np.array([eta,1-eta])])
        self.breakpoints=self.breaks
    def profile(self,s):
        s=np.atleast_1d(s).astype(float);A=np.zeros_like(s);V=A.copy();K=A.copy()
        early=s<self.ends[2]
        if np.any(early):A[early],V[early],K[early]=self.head.profile(s[early])
        for j in range(2,6):
            mask=(s>=self.ends[j])&((s<self.ends[j+1])if j<5 else(s<=self.end+1e-12))
            if not np.any(mask):continue
            l=s[mask]-self.ends[j];L=self.lengths[j];t=l/L
            if j in (2,4):
                a0=self.a_extra if j==2 else self.a_stop
                v0=self.v1 if j==2 else self.v2
                v1=self.v2 if j==2 else self.v3
                F,P,d=turn(t,self.eta)
                A[mask]=a0+v0*l+(v1-v0)*L*P
                V[mask]=v0+(v1-v0)*F;K[mask]=(v1-v0)*d/L
            elif j==3:A[mask]=self.a_turn+self.v2*l;V[mask]=self.v2
            else:
                S=t**3*(10-15*t+6*t*t);Sp=30*t*t*(1-t)**2;P=2.5*t**4-3*t**5+t**6
                H=-4*t**3+7*t**4-3*t**5;Hp=-12*t*t+28*t**3-15*t**4;HP=-t**4+1.4*t**5-.5*t**6
                A[mask]=self.a_bridge+self.v3*l+(self.final_v-self.v3)*L*P+L*L*self.final_acc*HP
                V[mask]=self.v3+(self.final_v-self.v3)*S+L*self.final_acc*H
                K[mask]=(self.final_v-self.v3)*Sp/L+self.final_acc*Hp
        return A,V,K


def linear_residual(profile,port,modes=1):
    from scipy.integrate import solve_ivp
    m=3*np.arange(1,modes+1);r=port['cut']['radius'];w=port['cut']['backgroundSlope'];D=np.asarray(port['linearSlope'][:modes])
    state=np.stack((-w*(r*D-m*m)/(m*m-1),np.ones(modes)),axis=1)
    state/=np.linalg.norm(state,axis=1)[:,None]
    def rhs(s,y):
        a,v,_=profile.profile([s]);a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
        z=y.reshape(modes,2);F=z[:,0];G=z[:,1]
        return np.stack((-(m*m-1)*v*F-m*m*b*G,(m*m-1)*v*v*F/b+m*m*v*G),axis=1).ravel()/a
    for low,high in reversed(list(zip(profile.breaks[:-1],profile.breaks[1:]))):
        z=solve_ivp(rhs,[high,low],state.ravel(),rtol=2e-9,atol=2e-11,method='DOP853',max_step=(high-low)/4)
        if not z.success:raise RuntimeError(z.message)
        state=z.y[:,-1].reshape(modes,2);state/=np.linalg.norm(state,axis=1)[:,None]
    return state[:,1]


def sampled_geometry(profile):
    s=np.unique(np.r_[np.linspace(0,profile.end,1601),profile.breaks]);a,v,acc=profile.profile(s)
    margin=float(np.min(1-v*v))
    if margin<=0:raise ValueError('Profile leaves positive meridian chart')
    b=np.sqrt(1-v*v)
    return dict(background_height=float(np.trapezoid(b,s)),background_radius=float(np.max(a)),
        background_kappa=float(np.max(np.maximum(abs(acc)/b,b/a))),background_root_min=margin,
        length=profile.end,minimum_radius=float(np.min(a)))


if __name__=='__main__':
    import argparse,json,itertools,time
    from pathlib import Path
    from scipy.optimize import brentq
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--port-file',type=Path,required=True);args=p.parse_args()
    port=json.loads(args.port_file.read_text());rows=[];roots=[];start=time.time()
    for ret,stop,L in itertools.product([.25,.4,.55,.7],[0.,.15,.3],[.4,.5,.6,.7]):
        previous=None
        for ac in np.linspace(1.,7.5,10):
            cfg=dict(return_speed=ret,stop_speed=stop,stop_acceleration=ac,final_length=L)
            try:
                f=ConsumedWindowLoop(**cfg);geo=sampled_geometry(f)
                if geo['background_kappa']>8.5:continue
                val=float(linear_residual(f,port)[0]);row=dict(parameters=cfg,residual=val,**geo);rows.append(row)
                if previous and previous[1]*val<0:
                    root=brentq(lambda z:linear_residual(ConsumedWindowLoop(**{**cfg,'stop_acceleration':z}),port)[0],previous[0],ac,xtol=1e-10)
                    fp=ConsumedWindowLoop(**{**cfg,'stop_acceleration':root});row=dict(parameters=fp.parameters,residual=linear_residual(fp,port,4).tolist(),**sampled_geometry(fp));roots.append(row);print(json.dumps(dict(event='root',**row)),flush=True)
                previous=(ac,val)
            except Exception as e:previous=None
        args.out.write_text(json.dumps(dict(scope=__doc__,rows=rows,roots=roots,seconds=time.time()-start),indent=2)+'\n')
    print(json.dumps(dict(event='complete',rows=len(rows),roots=len(roots),seconds=time.time()-start)),flush=True)
