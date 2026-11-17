"""A C3 meridian design retaining the old H strip and consuming its circle diamond.
Profile/background/characteristic diagnostics only; no nonlinear isometric
prefix, closed surface, reach certificate, or positive-K entrance theorem.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np
from scipy.integrate import quad


def turn(t,eta=.05):
    t=np.clip(np.asarray(t),0.,1.);z=np.minimum(t,1-t);x=z/eta;first=z<eta
    Fsmall=np.where(first,eta/(1-eta)*(x**3-x**4/2),(z-eta/2)/(1-eta))
    Psmall=np.where(first,eta*eta/(1-eta)*(x**4/4-x**5/10),(z*z/2-eta*z/2+.15*eta*eta)/(1-eta))
    d=np.where(first,(3*x*x-2*x**3)/(1-eta),1/(1-eta))
    return np.where(t<=.5,Fsmall,1-Fsmall),np.where(t<=.5,Psmall,.5-(1-t)+Psmall),d


class ConsumedWindowProfile:
    def __init__(self,delta=.07255,vu=.17,epsilon=.4,eta=.05,extra_speed=.38,extra_acceleration=1.,return_speed=.6,turn_acceleration=5.5,final_length=.2,cut_radius=.6,cut_w=.5,cut_wr=None):
        self.parameters=dict(delta=delta,vu=vu,epsilon=epsilon,eta=eta,extra_speed=extra_speed,extra_acceleration=extra_acceleration,return_speed=return_speed,turn_acceleration=turn_acceleration,final_length=final_length,cut_radius=cut_radius,cut_w=cut_w,cut_wr=-7*cut_w/cut_radius if cut_wr is None else cut_wr)
        self.delta=delta;self.vu=vu;self.eps=epsilon;self.eta=eta;self.Tu=delta/(vu*(1-epsilon));self.hold_end=(1-epsilon)*self.Tu;self.a_hold=1+delta*(1-1.5*epsilon)/(1-epsilon)
        L1=(extra_speed-vu)/(extra_acceleration*(1-eta));L2=(extra_speed+return_speed)/(turn_acceleration*(1-eta));self.v1=extra_speed;self.v2=-return_speed
        self.a_extra=self.a_hold+L1*(vu+extra_speed)/2;self.a_turn=self.a_extra+L2*(extra_speed-return_speed)/2
        self.final_v=-1/math.sqrt(1+cut_w*cut_w);self.final_acc=-cut_w*self.parameters['cut_wr']/(1+cut_w*cut_w)**2
        self.final_integral=final_length*(self.v2+self.final_v)/2-.1*final_length**2*self.final_acc
        coast=(self.a_turn+self.final_integral-cut_radius)/return_speed
        if min(L1,L2,coast,final_length)<=0:raise ValueError('Positive segment lengths required')
        self.lengths=np.array([self.hold_end,L1,L2,coast,final_length]);self.ends=np.r_[0.,np.cumsum(self.lengths)];self.end=float(self.ends[-1]);self.a_coast=self.a_turn+coast*self.v2
        self.breaks=np.unique(np.r_[self.ends,self.eps*self.Tu*np.array([eta,1-eta,1]),self.ends[1]+L1*np.array([eta,1-eta]),self.ends[2]+L2*np.array([eta,1-eta])])
    def profile(self,s):
        s=np.atleast_1d(s).astype(float);A=np.zeros_like(s);V=A.copy();K=A.copy()
        for j in range(5):
            mask=(s>=self.ends[j]-1e-14)&((s<self.ends[j+1])if j<4 else(s<=self.ends[j+1]+1e-12))
            if not np.any(mask):continue
            l=s[mask]-self.ends[j];L=self.lengths[j];t=l/L
            if j==0:
                u=s[mask]/self.Tu;inside=u<self.eps;F,P,d=turn(u/self.eps,self.eta);speed=np.where(inside,F,1.);I=np.where(inside,self.eps*P,u-self.eps/2)
                A[mask]=1+self.delta*I/(1-self.eps);V[mask]=self.vu*speed;K[mask]=np.where(inside,self.vu*d/(self.eps*self.Tu),0.)
            elif j in (1,2):
                a0=self.a_hold if j==1 else self.a_extra;v0=self.vu if j==1 else self.v1;v1=self.v1 if j==1 else self.v2;F,P,d=turn(t,self.eta)
                A[mask]=a0+v0*l+(v1-v0)*L*P;V[mask]=v0+(v1-v0)*F;K[mask]=(v1-v0)*d/L
            elif j==3:A[mask]=self.a_turn+self.v2*l;V[mask]=self.v2
            else:
                S=t**3*(10-15*t+6*t*t);Sp=30*t*t*(1-t)**2;P=2.5*t**4-3*t**5+t**6
                H=-4*t**3+7*t**4-3*t**5;Hp=-12*t*t+28*t**3-15*t**4;HP=-t**4+1.4*t**5-.5*t**6
                A[mask]=self.a_coast+self.v2*l+(self.final_v-self.v2)*L*P+L*L*self.final_acc*HP;V[mask]=self.v2+(self.final_v-self.v2)*S+L*self.final_acc*H;K[mask]=(self.final_v-self.v2)*Sp/L+self.final_acc*Hp
        return A,V,K
    def integral(self,fun,end):
        value=error=0.
        for lo,hi in zip(self.breaks[:-1],self.breaks[1:]):
            if lo>=end:break
            z,e=quad(fun,float(lo),float(min(hi,end)),epsabs=1e-11,epsrel=1e-11,limit=100);value+=z;error+=e
        return value,error
    def audit(self,R=2.,normal_width=.9,sH=.42):
        k=1/R;first_positive=float(self.ends[2])
        def speed(s):
            a,v,acc=self.profile([s]);return math.sqrt(max(float(acc[0]),0)/(float(a[0])*(k*k-float(v[0])**2)))
        chiH,errH=self.integral(speed,sH);chi0,err0=self.integral(speed,first_positive)
        def hloc(s):return math.sqrt(1-(float(self.profile([s])[1][0])/k)**2)
        zH,ez=self.integral(hloc,sH)
        def hbg(s):return math.sqrt(1-float(self.profile([s])[1][0])**2)
        z,ezbg=self.integral(hbg,self.end);ss=np.unique(np.r_[np.linspace(0,self.end,10001),self.breaks]);a,v,acc=self.profile(ss);root=1-v*v
        kap=np.maximum(abs(acc)/np.sqrt(root),np.sqrt(root)/a);arg=int(np.argmax(kap));hwidth=R*normal_width-2*chiH;remaining=R*normal_width-2*chi0
        jets=[]
        for b in self.ends[1:-1]:
            left=self.profile([b-1e-8]);right=self.profile([b+1e-8]);jets.append(dict(s=float(b),nearby_difference=[float(abs(left[j][0]-right[j][0]))for j in range(3)]))
        initial_radius=1+self.delta*self.eps/(2*(1-self.eps));initial_acceleration=self.vu/(self.eps*self.Tu*(1-self.eta))
        chi_lower=math.asin(self.vu/k)/math.sqrt(initial_radius*initial_acceleration)+(math.asin(self.v1/k)-math.asin(self.vu/k))/math.sqrt(self.a_extra*self.parameters['extra_acceleration'])
        return dict(scope=__doc__,characteristic_lower_bound_elementary=chi_lower,characteristic_lower_bound_margin=chi_lower-R*normal_width/2,initial_ramp_radius_upper=initial_radius,initial_ramp_acceleration_upper=initial_acceleration,extra_ramp_radius_upper=self.a_extra,parameters=self.parameters,lengths=self.lengths.tolist(),segment_ends=self.ends.tolist(),first_positive_K_begins=first_positive,core_radius=R,core_normal_width=normal_width,core_material_width=R*normal_width,characteristic_loss_at_H=chiH,characteristic_loss_at_first_positive_K=chi0,characteristic_quad_error_sum=err0,remaining_window_at_H=hwidth,remaining_window_at_first_positive_K=remaining,circle_diamond_consumed_before_first_positive_K=remaining<0,held_vertical_diameter=2*zH,background_height=z,background_radius_max=float(np.max(a)),background_speed_max=float(np.max(abs(v))),background_curvature_sample_max=float(np.max(kap)),background_curvature_arg_s=float(ss[arg]),cut_jets=[float(t[0])for t in self.profile([self.end])],join_nearby_twojet_differences=jets,scope_limits='No nonlinear surface generated. Negative remaining window means only that the known characteristic uniqueness diamond has ended; it does not prove loss of all local symmetry or sufficient elliptic Cauchy compatibility.')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);p.add_argument('--extra-speed',type=float,default=.38);p.add_argument('--return-speed',type=float,default=.6);p.add_argument('--turn-acceleration',type=float,default=5.5);p.add_argument('--final-length',type=float,default=.2);p.add_argument('--radius',type=float,default=2.);p.add_argument('--normal-width',type=float,default=.9);a=p.parse_args()
    f=ConsumedWindowProfile(extra_speed=a.extra_speed,return_speed=a.return_speed,turn_acceleration=a.turn_acceleration,final_length=a.final_length);out=f.audit(a.radius,a.normal_width);a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['join_nearby_twojet_differences']},indent=2))
