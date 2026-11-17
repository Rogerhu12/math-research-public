#!/usr/bin/env python3
"""Same exact Hold scalar through its inward planar cuff, with integer boxes.

The .99 source jet is the exact stored scalar knot, enclosed by the already
published R636 boxes. Ramp integrals use fixed composite Simpson panels and
an explicit fourth-derivative remainder; constant curvature uses exact
trigonometric primitives. Stored floating alpha/K/S/R are never new initial
data. This is a scalar oracle, not a surface or a nonlinear solution.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import bisect,hashlib,importlib.util

ORACLE_SHA='babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'
HOLD_SHA='ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

class FullHold:
    def __init__(self,data,oracle_source,hold_source,panels=128):
        if sha(oracle_source)!=ORACLE_SHA or sha(hold_source)!=HOLD_SHA:
            raise ValueError('Changed exact scalar dependency')
        if not isinstance(panels,int)or panels<1:raise ValueError('Positive fixed Simpson panel count required')
        spec=importlib.util.spec_from_file_location('full_hold_integer_oracle',oracle_source)
        self.o=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.o)
        self.h=self.o.h;h=self.h;o=self.o;self.panels=panels
        self.source_sha=sha(__file__);self.hold_sha=HOLD_SHA;self.oracle_sha=ORACLE_SHA
        self.origin=Q(float(data['analytic_extension_origin']));self.cut=Q(.995)
        geometry=data['fixed_scalar_profile']['geometry'];self.knots=geometry['knots']
        if self.origin!=Q(float(self.knots[-1]['s'])):raise ValueError('Wrong exact analytic origin')
        self.x=[Q(float(k['s']))for k in self.knots]
        jets=[tuple(Q(float(k[v]))for v in ('a','ap','app'))for k in self.knots]
        law=geometry['initial_law'];L,v,k=(Q(float(law[n]))for n in ('length','velocity','k0'))
        s=self.x[0];u=s/L;b=k*L;c=3*v-2*b;d=b-2*v
        jets[0]=(1+L*(b*u*u/2+c*u**3/3+d*u**4/4),b*u+c*u*u+d*u**3,(b+2*c*u+3*d*u*u)/L)
        if self.x[0]!=0 or jets[0][0]!=1:raise ValueError('Declared core scalar must start at one')
        self.coefficients=[];ap_bound=Q(0)
        for i in range(len(self.x)-1):
            width=self.x[i+1]-self.x[i];left,right=jets[i],jets[i+1]
            c0,c1,c2=left[0],width*left[1],width*width*left[2]/2
            a=right[0]-c0-c1-c2;b=width*right[1]-c1-2*c2;c=width*width*right[2]-2*c2
            co=[c0,c1,c2,10*a-4*b+c/2,-15*a+7*b-c,6*a-3*b+c/2]
            self.coefficients.append(co)
            dc=[Q(j+1)*co[j+1]/width for j in range(5)]
            bez=[sum((dc[j]*Q(comb(q,j),comb(4,j))for j in range(q+1)),Q(0))for q in range(5)]
            ap_bound=max(ap_bound,max(abs(z)for z in bez))
        self.old_ap_bound=ap_bound
        if ap_bound>=1:raise ValueError('The scalar uncertainty transport uses the verified old |a_s|<1')
        a0=o.box('1.16660641061202','1.16660641061204')
        v0=o.box('.35794863891029','.35794863891032')
        u0=o.box('-2.01012061072760','-2.01012061072757')
        for box,name in [(a0,'a'),(v0,'ap'),(u0,'app')]:
            if not o.contains(box,Q(float(self.knots[-1][name]))):raise ValueError('Original jet missed its established enclosure')
        self.a0=a0;self.K=o.divide(h.neg(u0),o.square_root(o.subtract(h.interval(Q(1)),h.multiply(v0,v0))))
        if not Q(3,2)<Q(self.K[0],h.S)<=Q(self.K[1],h.S)<Q(2153,1000):raise ValueError('K derivative budget failed')
        self.alpha_origin=o.arcsine(v0);self.alpha_cut=o.subtract(self.alpha_origin,h.scale(self.K,self.cut-self.origin))
        self.ac=h.add(a0,o.divide(o.subtract(h.sine_cosine(self.alpha_cut)[1],h.sine_cosine(self.alpha_origin)[1]),self.K))
        self.f,self.hold,self.rise,self.out=Q(.002),Q(.02),Q(.02),Q(.02)
        self.kn,self.kp=Q(-5,2),Q(3,2)
        A1=o.subtract(self.alpha_cut,h.scale(h.add(self.K,h.interval(self.kn)),self.f/2))
        A2=o.subtract(A1,h.interval(self.kn*self.hold))
        A3=o.subtract(A2,h.interval((self.kn+self.kp)*self.rise/2))
        self.pi=h.pi_interval();A4=h.add(h.scale(self.pi,-Q(1,2)),h.interval(self.kp*self.out/2))
        self.plateau=h.scale(o.subtract(A3,A4),1/self.kp)
        if self.plateau[0]<=0:raise ValueError('Nonpositive exact plateau')
        fixed_end=self.cut+self.f+self.hold+self.rise
        self.time=[h.interval(self.cut),h.interval(self.cut+self.f),h.interval(self.cut+self.f+self.hold),h.interval(fixed_end)]
        self.time.append(h.add(self.time[-1],self.plateau));self.time.append(h.add(self.time[-1],h.interval(self.out)))
        self.S=self.time[-1]
        self.alpha=[self.alpha_cut,A1,A2,A3,A4,h.scale(self.pi,-Q(1,2))]
        self.ramps={0:self.Ramp(self,self.alpha_cut,self.K,h.interval(self.kn),self.f,Q(5,2),Q(4653,1000)),
                    2:self.Ramp(self,A2,h.interval(self.kn),h.interval(self.kp),self.rise,Q(5,2),Q(4)),
                    4:self.Ramp(self,A4,h.interval(self.kp),h.interval(Q(0)),self.out,Q(3,2),Q(3,2))}
        self.position=[(self.ac,(0,0))]
        for j in range(5):
            if j in self.ramps:delta=self.ramps[j].prefix[-1]
            else:delta=self.constant_end(self.alpha[j],self.alpha[j+1],self.kn if j==1 else self.kp)
            self.position.append(tuple(h.add(a,b)for a,b in zip(self.position[-1],delta)))
        self.R,self.height_increment=self.position[-1]
        if self.R[0]<=0:raise ValueError('The exact planar radius did not stay positive')
        self.boundaries=[(h.interval(self.origin),self.a0,None)]+[(t,p[0],p[1])for t,p in zip(self.time,self.position)]

    @staticmethod
    def P(u):return Q(0)if u<=0 else u-Q(1,2)if u>=1 else Q(5,2)*u**4-3*u**5+u**6

    class Ramp:
        def __init__(self,parent,alpha,left,right,width,km,delta):
            self.parent=parent;self.alpha=alpha;self.left=left;self.right=right;self.width=width
            p=parent.panels;self.step=width/p;h=parent.h
            k1=delta*Q(15,8)/width;k2=delta*6/width**2;k3=delta*60/width**3
            self.derivative4=km**4+3*k1*k1+4*km*k2+6*km*km*k1+k3
            self.error_panel=self.derivative4*self.step**5/2880
            self.prefix=[((0,0),(0,0))]
            prior=h.sine_cosine(self.angle(Q(0)))
            for j in range(p):
                middle=h.sine_cosine(self.angle(self.step*(Q(j)+Q(1,2))))
                final=h.sine_cosine(self.angle(self.step*(j+1)))
                values=[]
                for k in (0,1):
                    average=h.add(h.add(prior[k],h.scale(middle[k],4)),final[k])
                    inc=h.add(h.scale(average,self.step/6),parent.o.box(-self.error_panel,self.error_panel))
                    values.append(h.add(self.prefix[-1][k],inc))
                self.prefix.append(tuple(values));prior=final
        def angle(self,t):
            p=self.parent;h=p.h;u=t/self.width;P=p.P(u)
            return p.o.subtract(self.alpha,h.add(h.scale(self.left,self.width*(u-P)),h.scale(self.right,self.width*P)))
        def integral(self,tbox):
            p=self.parent;h=p.h
            low=max(Q(0),Q(tbox[0],h.S));high=min(self.width,Q(tbox[1],h.S))
            if low>high:raise ValueError('Partial ramp time interval is outside its exact segment')
            t=(low+high)/2;radius=max(t-low,high-t)
            j=min(p.panels,int(t//self.step));start=j*self.step
            result=self.prefix[j]
            if t>start:
                width=t-start;v0=h.sine_cosine(self.angle(start));vm=h.sine_cosine(self.angle((start+t)/2));v1=h.sine_cosine(self.angle(t))
                error=self.derivative4*width**5/2880;new=[]
                for k in (0,1):
                    value=h.scale(h.add(h.add(v0[k],h.scale(vm[k],4)),v1[k]),width/6)
                    new.append(h.add(result[k],h.add(value,p.o.box(-error,error))))
                result=tuple(new)
            return tuple(h.add(v,p.o.box(-radius,radius))for v in result)

    def constant_end(self,alpha0,alpha1,k):
        h=self.h;o=self.o;s0,c0=h.sine_cosine(alpha0);s1,c1=h.sine_cosine(alpha1)
        return h.scale(o.subtract(c1,c0),1/k),h.scale(o.subtract(s0,s1),1/k)

    def old_exact(self,s):
        i=min(len(self.x)-2,max(0,bisect.bisect_right(self.x,s)-1));u=(s-self.x[i])/(self.x[i+1]-self.x[i])
        out=Q(0)
        for value in reversed(self.coefficients[i]):out=out*u+value
        return out

    def at_box(self,sbox):
        """Enclose a and the reference height increment from the cut.

        A queried exact point may itself be specified by a rigorous box
        (for example an affine expression in the exact nonbinary S).
        |a_s|,|z_s|<=1 on the Hold extension transports that uncertainty.
        """
        h=self.h;o=self.o;lo,hi=Q(sbox[0],h.S),Q(sbox[1],h.S)
        if lo<0 or hi>Q(self.S[1],h.S):raise ValueError('Outside the fixed full scalar domain')
        if hi<=self.origin:
            mid=(lo+hi)/2;value=self.old_exact(mid);err=self.old_ap_bound*(hi-lo)/2
            return o.box(value-err,value+err),None
        for t,a,z in self.boundaries:
            tl,th=Q(t[0],h.S),Q(t[1],h.S)
            if lo<=th and hi>=tl:
                fee=max(abs(lo-th),abs(hi-tl))
                return h.add(a,o.box(-fee,fee)),None if z is None else h.add(z,o.box(-fee,fee))
        mid=(lo+hi)/2
        if hi<self.cut:
            angle=o.subtract(self.alpha_origin,h.scale(self.K,mid-self.origin))
            rad=h.add(self.a0,o.divide(o.subtract(h.sine_cosine(angle)[1],h.sine_cosine(self.alpha_origin)[1]),self.K))
            return h.add(rad,o.box(-(hi-lo)/2,(hi-lo)/2)),None
        j=next((k for k in range(5)if lo>Q(self.time[k][1],h.S)and hi<Q(self.time[k+1][0],h.S)),None)
        if j is None:raise ValueError('Scalar stage was not assigned to one exact segment')
        tbox=o.subtract(sbox,self.time[j])
        if j in self.ramps:delta=self.ramps[j].integral(tbox)
        else:
            k=self.kn if j==1 else self.kp
            angle=o.subtract(self.alpha[j],h.scale(tbox,k));delta=self.constant_end(self.alpha[j],angle,k)
        return tuple(h.add(a,b)for a,b in zip(self.position[j],delta))

    def point_box(self,value):return self.h.interval(Q(value))
    def affine_time(self,coefficient,constant):return self.h.add(self.h.scale(self.S,Q(coefficient)),self.h.interval(Q(constant)))
    def carrier(self,box):return float(Q(box[0]+box[1],2*self.h.S))
    def enclosure(self,box):return self.o.enclosure(box)
    def metadata(self):
        return dict(source_sha256=self.source_sha,integer_oracle_sha256=self.oracle_sha,hold_source_sha256=self.hold_sha,
            origin_exact=str(self.origin),cut_exact=str(self.cut),durations_exact=[str(v)for v in (self.f,self.hold,self.rise,self.out)],
            K=self.enclosure(self.K),alpha_cut=self.enclosure(self.alpha_cut),cut_radius=self.enclosure(self.ac),
            plateau=self.enclosure(self.plateau),S=self.enclosure(self.S),R=self.enclosure(self.R),
            reference_height_increment=self.enclosure(self.height_increment),old_absolute_a_s_bound_exact=str(self.old_ap_bound),
            simpson_panels_per_ramp=self.panels,
            ramp_fourth_derivative_bounds={str(j):str(r.derivative4)for j,r in self.ramps.items()},
            ramp_total_simpson_error_exact={str(j):str(self.panels*r.error_panel)for j,r in self.ramps.items()},
            arithmetic='R636 integer/Fraction outward 10^-24 boxes; exact old quintics and Simpson remainder',
            target_definition='Same exact .99 nodal jet -> .995 transport -> .002/-2.5/.02/.02/+1.5/plateau/.02 Hold',
            stored_floating_alpha_K_S_R_used_as_target=False,nonlinear_surface_solve=False)
