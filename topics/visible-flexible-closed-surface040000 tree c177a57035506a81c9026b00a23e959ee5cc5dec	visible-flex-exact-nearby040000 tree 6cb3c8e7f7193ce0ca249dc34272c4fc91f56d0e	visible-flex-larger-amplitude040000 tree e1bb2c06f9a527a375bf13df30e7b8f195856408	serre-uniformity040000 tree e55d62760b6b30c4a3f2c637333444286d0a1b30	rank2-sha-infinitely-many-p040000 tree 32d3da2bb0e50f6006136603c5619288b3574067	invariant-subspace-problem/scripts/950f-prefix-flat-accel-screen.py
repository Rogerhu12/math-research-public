#!/usr/bin/env python3
"""Linear screen of new meridian metrics with a near-constant acceleration ramp.

All amplitude/diameter comparisons below are first-order heuristics, not
nonlinear isometries or reach certificates. The actual weighted tail is held
fixed, while each meridian configuration is a different metric design.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import cumulative_trapezoid


def turn_ramp(t,eta=.1):
    """F integral of a C1 flat-topped acceleration, and its primitive P.
    F(0)=0,F(1)=1,F'=0 at endpoints; max F'=1/(1-eta).
    F(1-t)=1-F(t), hence integral_0^1 F=1/2.
    """
    t=np.clip(np.asarray(t),0.,1.);z=np.minimum(t,1-t);x=z/eta
    first=z<eta
    Fsmall=np.where(first,eta/(1-eta)*(x**3-x**4/2),(z-eta/2)/(1-eta))
    Psmall=np.where(first,eta*eta/(1-eta)*(x**4/4-x**5/10),(z*z/2-eta*z/2+.15*eta*eta)/(1-eta))
    d=np.where(first,(3*x*x-2*x**3)/(1-eta),1/(1-eta))
    F=np.where(t<=.5,Fsmall,1-Fsmall);P=np.where(t<=.5,Psmall,.5-(1-t)+Psmall)
    return F,P,d


def ramp(u,eps,eta=.1):
    u=np.asarray(u);up=u<eps;down=u>1-eps;t=np.where(up,u/eps,(1-u)/eps);F,P,d=turn_ramp(t,eta)
    w=np.where(up|down,F,1.);I=np.where(up,eps*P,np.where(down,1-eps-eps*P,u-eps/2));wp=np.where(up,d/eps,np.where(down,-d/eps,0.))
    return w,I,wp


def build_flow():
    from fixed_metric_mode3_flow import PlanarSymmetryFlow
    class FlatFlow(PlanarSymmetryFlow):
        def prefix_profile(self,s):
            s=np.asarray(s);t=np.mod(s,self.period);outward=self.direction=='outward';first=self.Tu if outward else self.Td;second=self.Td if outward else self.Tu;isfirst=t<first
            u=np.where(isfirst,t/first,(t-first)/second);w,I,wp=ramp(u,self.eps,self.cfg.get('ramp_eta',.1));sign=1 if outward else -1;vfirst=self.vu if outward else self.vd;vsecond=self.vd if outward else self.vu
            aa=np.where(isfirst,1+sign*self.delta*I/(1-self.eps),1+sign*self.delta-sign*self.delta*I/(1-self.eps));ap=np.where(isfirst,sign*vfirst*w,-sign*vsecond*w);app=np.where(isfirst,sign*vfirst*wp/first,-sign*vsecond*wp/second)
            return aa,ap,app
    return FlatFlow,PlanarSymmetryFlow


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();N=Path(__file__).resolve().parent.parent/'notes';sys.path[:0]=[str(N),str(a.source_root/'topics/large-amplitude-twist-flex/scripts')];Flat,Cos=build_flow();port=json.loads(a.port.read_text())
    configs=[]
    for law,eps in [('cosine',.4),('flat',.4),('flat',.48)]:
        for vu in [.15,.2,.25,.3,.35]:
            for vd in [.3,.4,.5,.6]:configs.append(dict(direction='outward',vu=vu,vd=vd,ramp=eps,cycles=1,cut_radius=.6,cut_slope=.5,ramp_law=law,ramp_eta=.1))
    for vu,vd in [(.35,.5),(.4,.55),(.45,.6),(.5,.65),(.5,.7),(.55,.7),(.55,.75)]:
        for eps in [.4,.45,.48]:configs.append(dict(direction='outward',vu=vu,vd=vd,ramp=eps,cycles=2,cut_radius=.6,cut_slope=.5,ramp_law='flat',ramp_eta=.1))
    report=dict(scope=__doc__,port=str(a.port),rows=[]);begin=time.time()
    for index,cfg in enumerate(configs):
        cls=Flat if cfg['ramp_law']=='flat'else Cos
        def calc(delta):
            f=cls({**cfg,'delta':float(delta)},port,1,.001,32,3);return f,f.backward_line()
        def scalar(delta):return float(calc(delta)[1].core[1])
        roots=[];prev=None;errors=[]
        for delta in [.012,.02,.03,.045,.06,.08,.10,.12,.15,.19,.25]:
            try:
                z=scalar(delta)
                if prev and z*prev[1]<0:
                    d=brentq(scalar,prev[0],delta,xtol=2e-11);f,line=calc(d);s=np.unique(np.r_[np.linspace(0,f.end,1201),f.breaks]);fg=np.empty((2,len(s)))
                    for j,(lo,hi,sol,scale)in enumerate(line.segments):
                        mask=(s>=lo)&((s<hi)if j+1<len(line.segments)else(s<=hi))
                        if np.any(mask):fg[:,mask]=sol(s[mask])*math.exp(scale-line.logscale)/line.core[0]
                    aa,ap,app=f.profile(s);b=np.sqrt(1-ap*ap);height=cumulative_trapezoid(b,s,initial=0.);K=float(np.maximum(abs(app)/b,b/aa).max());gain=float(fg[1,-1]);budgets=[]
                    for q in [.08,.10,.105]:
                        ell=2*q;R2=np.maximum((aa+q*fg[0])**2+(height+ell+q*fg[1])**2,(aa-q*fg[0])**2+(height+ell-q*fg[1])**2);D=2*math.sqrt(float(R2.max()));Kcore=1/(1-8*q)
                        budgets.append(dict(q_support=q,ell=ell,linear_cut_height=q*abs(gain),linear_sample_ball_D=D,comparison_hold_ratio=2*q/D,comparison_background_KD=K*D,comparison_core_KD=Kcore*D))
                    roots.append(dict(config={**cfg,'delta':d},gain=gain,background_height=float(height[-1]),background_kappa_sample=K,meridian_length=f.end,budgets=budgets))
                prev=(delta,z)
            except Exception as e:errors.append(dict(delta=delta,error=repr(e)));prev=None
        report['rows'].append(dict(config=cfg,roots=roots,errors=errors));report['seconds']=time.time()-begin;a.out.write_text(json.dumps(report,indent=2)+'\n')
        if index%10==0:print(json.dumps(dict(index=index,total=len(configs),roots=len(roots),seconds=report['seconds'])),flush=True)
    allrows=[dict(config=r['config'],gain=r['gain'],K=r['background_kappa_sample'],**b)for item in report['rows']for r in item['roots']for b in r['budgets']]
    feasible=[r for r in allrows if r['comparison_hold_ratio']>=.05 and max(r['comparison_background_KD'],r['comparison_core_KD'])<=33.3333333]
    feasible.sort(key=lambda r:r['linear_cut_height']);report['ranked_budget_candidates']=feasible[:20];a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(event='complete',candidate_count=len(feasible),top=feasible[:5])),flush=True)

if __name__=='__main__':main()
