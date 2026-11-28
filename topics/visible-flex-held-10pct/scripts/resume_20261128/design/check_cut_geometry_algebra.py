#!/usr/bin/env python3
"""Independent 75-digit implementation check for complete cut repair algebra.

These small literal arrays are synthetic finite Fourier data, not an accepted
prefix or tail.  The checks exercise unequal mode sets, the height zero mode,
both signs of planar frequency, angular order three, right-endpoint Hermite
weights and the complete D2 Gram chain.  They provide no surface certificate.
"""
import hashlib
import json
from pathlib import Path
import resource
import sys
from types import SimpleNamespace
import mpmath as mp
import numpy as np

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'geometry/cartesian_prefix_cut_metric.py'
sys.path.insert(0,str(SOURCE.parent))
digest=lambda path:hashlib.sha256(Path(path).read_bytes()).hexdigest()
source_hash=digest(SOURCE)
import cartesian_prefix_cut_metric as c
if digest(SOURCE)!=source_hash:
    raise RuntimeError('The reviewed source changed during import')

mp.mp.dps=75
Q=c.Q
I=c.I


def m(value):
    value=Q(value) if isinstance(value,(Q,int)) else Q.from_float(float(value))
    return mp.mpf(value.numerator)/value.denominator


counts={}


def contains(interval,value,kind):
    lower,upper=map(float,interval.x)
    if not m(lower)<=value<=m(upper):
        raise ArithmeticError('%s failed: %r <= %s <= %r' % (kind,lower,value,upper))
    counts[kind]=counts.get(kind,0)+1


def main():
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
    pp=np.array([-5,-2,1,4,10]);ph=np.array([0,3,9])
    tp=np.array([-8,-2,1,7,13]);th=np.array([0,6,9,12])
    prefix=np.arange(1,3*(len(pp)+len(ph))+1,dtype=float).reshape(3,-1)/2**13
    tail=np.arange(2,3*(len(tp)+len(th))+2,dtype=float).reshape(3,-1)/2**15
    prefix[:,::2]*=-1;tail[:,1::2]*=-1
    prefix[0,list(pp).index(1)]=.3000123
    prefix[0,len(pp)]=.84375
    tail[0,len(tp)]=.03125
    R,w=.3,.08
    pm,hm,coeff,definition=c.complete_cut_coefficients(prefix,pp,ph,tail,tp,th,R,w)
    assert set(pm)==set(pp)|set(tp) and set(hm)==set(ph)|set(th)
    zero_index=len(pm)+list(hm).index(0)
    assert np.array_equal(coeff.x[0][0,zero_index],np.array(0.))
    assert np.array_equal(coeff.x[1][0,zero_index],np.array(0.))
    RR,ww=m(R),m(w);wr=-7*ww/RR
    ap=-1/mp.sqrt(1+ww*ww);app=-ww*wr/(1+ww*ww)**2
    zcut=m(prefix[0,len(pp)]);mean=m(tail[0,len(tp)])

    def vector(data,planar,height,order,psi,angular=0):
        xy=sum((m(data[order,j])*(1j*int(k))**angular*mp.exp(1j*int(k)*psi)
                for j,k in enumerate(planar)),mp.mpc(0))
        zz=sum((m(data[order,len(planar)+j])*int(k)**angular*
                mp.cos(int(k)*psi+angular*mp.pi/2) for j,k in enumerate(height)),mp.mpf(0))
        return [mp.re(xy),mp.im(xy),zz]

    def difference(radial,psi,angular=0):
        A=[vector(tail,tp,th,j,psi,angular) for j in range(3)]
        circle=mp.exp(1j*psi)*(1j)**angular
        er=[mp.re(circle),mp.im(circle),mp.mpf(0)]
        F0=[RR*er[0]+A[0][0],RR*er[1]+A[0][1],-A[0][2]]
        F1=[er[0]+A[1][0],er[1]+A[1][1],-A[1][2]]
        F2=[A[2][0],A[2][1],-A[2][2]]
        if angular==0:
            F0[2]+=zcut+mean;F1[2]-=ww;F2[2]-=wr
        targets=[F0,[ap*v for v in F1],
                 [ap*ap*v+app*u for v,u in zip(F2,F1)]]
        old=vector(prefix,pp,ph,radial,psi,angular)
        return [v-u for v,u in zip(targets[radial],old)]

    N=32
    left=[2*mp.pi*j/(3*N) for j in range(N)]
    right=[2*mp.pi*(j+1)/(3*N) for j in range(N)]
    boxes=I(np.array([c.K.dn(float(x)) for x in left]),
            np.array([c.K.up(float(x)) for x in right]))
    width=I(c.K.dn(float(2*mp.pi/(3*N))),c.K.up(float(2*mp.pi/(3*N))))
    tables=c.cut_angular_tables(pm,hm,coeff,N,boxes,width)
    for index in range(N):
        for angular in range(4):
            for radial in range(3):
                for xyz,value in enumerate(difference(radial,left[index],angular)):
                    contains(tables[f'point_cut_{angular}'].item((radial,index,xyz)),value,
                             'point_complete_cartesian_derivative')
                for fraction in (mp.mpf(0),mp.mpf(1)/7,mp.mpf(1)/2,mp.mpf(6)/7,mp.mpf(1)):
                    psi=left[index]+fraction*(right[index]-left[index])
                    for xyz,value in enumerate(difference(radial,psi,angular)):
                        contains(tables[f'box_cut_{angular}'].item((radial,index,xyz)),value,
                                 'box_complete_cartesian_derivative')

    fake=c.CutMetric.__new__(c.CutMetric)
    fake.cut_width=Q.from_float(.04);fake.target=SimpleNamespace(end=Q(2))
    fake.cut_start=fake.target.end-fake.cut_width;fake.width=Q(1,10)
    L=m(fake.cut_width);end=m(fake.target.end)

    def weight(j,s):
        t=(end-s)/L
        # Independently expanded endpoint cardinal polynomials.
        H=((1-t)**3*(1+3*t+6*t*t),t*(1-t)**3*(1+3*t),t*t*(1-t)**3/2)
        return (-L)**j*H[j]

    def mul_poly(a,b):
        z=[Q(0)]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):z[i+j]+=x*y
        return z

    vanishing=[Q(1),Q(-3),Q(3),Q(-1)]
    exact_polys=[mul_poly(vanishing,[Q(1),Q(3),Q(6)]),
                 mul_poly(vanishing,[Q(0),Q(1),Q(3)]),
                 mul_poly(vanishing,[Q(0),Q(0),Q(1,2)])]

    def exact_weight_derivative(j,s,order):
        t=(fake.target.end-s)/fake.cut_width
        poly=list(exact_polys[j])
        for _ in range(order):poly=[(d+1)*poly[d+1] for d in range(len(poly)-1)]
        return ((-1)**(j+order)*fake.cut_width**(j-order)*
                sum((a*t**d for d,a in enumerate(poly)),Q(0)))

    for q in (Q(0),Q(1,7),Q(1,2),Q(6,7),Q(1)):
        s=fake.cut_start+q*fake.cut_width
        W=fake.cut_weights(I.rational(s),s,s)
        for order in range(4):
            for j in range(3):
                # At the zero-extension join the helper chooses the left
                # third jet. Only orders <=2 are shared by the C2 map.
                expected=Q(0) if s==fake.cut_start else exact_weight_derivative(j,s,order)
                contains(W[order][j],m(expected),
                         'right_hermite_derivative')
    for j in range(3):
        for order in range(3):
            assert exact_weight_derivative(j,fake.target.end,order)==int(j==order)
            assert exact_weight_derivative(j,fake.cut_start,order)==0

    # One genuine angular batch and one radial piece, with all cut modes.
    k=17;fake.P=len(pp);fake.pm=pp;fake.hm=ph
    fake.tables={name:value.item((slice(None),slice(k,k+1),slice(None)))
                 for name,value in tables.items()}
    angle_intervals={'point':I(c.K.dn(float(left[k])),c.K.up(float(left[k]))),
                     'box':boxes.item(slice(k,k+1))}
    for tag,angle in angle_intervals.items():
        if np.ndim(angle.x[0])==0:
            angle=I(np.asarray([angle.x[0]]),np.asarray([angle.x[1]]))
        ps,pc=c.exact_sincos(I(pp[:,None])*angle)
        hs,hc=c.exact_sincos(I(ph[:,None])*angle)
        for order in range(4):
            fake.tables[f'{tag}_basis_{order}_0']=[pc,-ps,-pc,ps][order]*I(pp[:,None]**order)
            fake.tables[f'{tag}_basis_{order}_1']=[ps,pc,-ps,-pc][order]*I(pp[:,None]**order)
            fake.tables[f'{tag}_basis_{order}_2']=[hc,-hs,-hc,hs][order]*I(ph[:,None]**order)
            fake.tables[f'{tag}_lift_{order}']=I(np.zeros((1,3)))
            fake.tables[f'{tag}_center_{order}']=I(np.zeros((3,1,3)))
        sn,co=c.exact_sincos(3*angle)
        fake.tables[f'{tag}_trig_0']=sn;fake.tables[f'{tag}_trig_1']=co

    class Polynomial:
        def __init__(self,coefficients):self.c=coefficients
        def values(self,s,l,r):
            coefficients=[I(v) for v in self.c];answer=[]
            for order in range(4):
                value=I(0)
                for cc in coefficients[::-1]:value=value*s+cc
                answer.append(value)
                coefficients=[(j+1)*coefficients[j+1] for j in range(len(coefficients)-1)]
                if not coefficients:coefficients=[I(np.zeros_like(answer[0].x[0]))]
            return answer

    base=prefix[0].copy()
    base[list(pp).index(1)]=1.
    polynomial=[base,np.ones_like(base)/2**15,-np.arange(len(base))/2**17]
    fake.field=Polynomial(polynomial)
    fake.lift=Polynomial([np.array([0.])])
    fake.chart=Polynomial([np.array([.04]),np.array([.02]),np.array([.005])])
    radius=Polynomial([np.array(1.),np.array(.1),np.array(.01)])
    fake.target.jets=radius.values

    def position(s,psi):
        values=np.zeros((1,len(base)),dtype=object)
        values[0]=[sum(m(cc[j])*s**d for d,cc in enumerate(polynomial)) for j in range(len(base))]
        # Do not round these mpmath coefficients through the literal reader.
        xy=sum(values[0,j]*mp.exp(1j*int(mode)*psi) for j,mode in enumerate(pp))
        zz=sum(values[0,len(pp)+j]*mp.cos(int(mode)*psi) for j,mode in enumerate(ph))
        v=[mp.re(xy),mp.im(xy),zz]
        for j in range(3):
            D=difference(j,psi)
            v=[a+weight(j,s)*b for a,b in zip(v,D)]
        return v

    def gram(s,psi):
        xs=[mp.diff(lambda z:position(z,psi)[j],s) for j in range(3)]
        xp=[mp.diff(lambda z:position(s,z)[j],psi) for j in range(3)]
        ee=m(.04)+m(.02)*s+m(.005)*s*s
        ep=m(.02)+2*m(.005)*s
        aa=1+m(.1)*s+m(.01)*s*s
        rho=1-ee*mp.cos(3*psi);theta_s=-ep*mp.sin(3*psi)/3
        u=[a-theta_s/rho*b for a,b in zip(xs,xp)];v=[b/(aa*rho) for b in xp]
        return [sum(a*a for a in u)-1,sum(a*b for a,b in zip(u,v)),sum(a*a for a in v)-1]

    sl=fake.cut_start+fake.cut_width*Q(2,7);sr=fake.cut_start+fake.cut_width*Q(3,7)
    for axis,tag in [('radial','point'),('angular','box')]:
        observed,_=fake.evaluate(sl,sr,tag,axis)
        for sf in (Q(0),Q(1,2),Q(1)):
            s=m(sl+sf*(sr-sl))
            angles=[left[k]] if axis=='radial' else [left[k],(left[k]+right[k])/2,right[k]]
            for psi in angles:
                for component in range(3):
                    for order,attr in enumerate(('v','d','d2')):
                        fun=(lambda z:gram(z,psi)[component]) if axis=='radial' else (lambda z:gram(s,z)[component])
                        value=mp.diff(fun,s if axis=='radial' else psi,order)
                        contains(getattr(observed[component],attr).item(0),value,'complete_D2_Gram_'+axis)
    report=dict(scope=__doc__,status='small_independent_75_digit_checks_passed',
        source_sha256_loaded=source_hash,source_sha256_at_return=digest(SOURCE),
        source_changed_while_checking=digest(SOURCE)!=source_hash,
        checker_sha256=digest(__file__),counts=counts,
        union_planar_modes=pm.tolist(),union_height_modes=hm.tolist(),
        exact_height_zero_value_cancellation=True,definition=definition,
        interval_kernel_not_reproved_by_samples=True,actual_surface_input=False,
        solver_invoked=False,accepted_field_produced=False,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    (out/'review.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
