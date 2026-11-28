"""Use original n>=0 Peano receipts to bound the entire omitted infinite annular sectors."""
import numpy as np
from r734_true_dyadic_tail import I,D,B,L0,ONE,ZERO,HIGH,monotone_trans
from r735_paid_tail_beta_envelope import cap_mode,as_matrix,mv
from r738_negative_tail_and_macro_source import FIRST


def upper(v):return I(I(v).norm())


def deeper_amplitude(s,j,port,source,book):
    """Change from new-cut f=1 to original-cut f, retaining all projective denominators."""
    k=j*j;steps=port['negative_cells']
    def line(n):
        raw=steps[str(n)]['line'] if n<0 else source[f'side{s}_m{j}_n0_accepted_line']['data']['line']
        return tuple(I(*a) for a in raw)
    a=FIRST[s];rat=B/(B-s*L0/(I(2)**a))
    amp=(rat**k)/line(a)[0]
    for n in range(a,0):
        m=as_matrix(book.records[f'side{s}_m{j}_n{n}_depth{steps[str(n)]["depth"]}_complete']['data'])
        v=line(n);vp=line(n+1)
        pivot=0 if v[0].lo==v[0].hi==1 else 1
        if v[pivot].lo!=1 or v[pivot].hi!=1:raise ArithmeticError('Unnormalized new-cell pivot.')
        amp=16*amp/mv((m[3],-m[1],-m[2],m[0]),vp)[pivot]
    return amp*((B-s*L0)/B)**k*line(0)[0]


def deep_cost(s,j,port,source,book):
    cap=cap_mode(j,s,source,book);N=cap['N'];factor=upper(deeper_amplitude(s,j,port,source,book))
    rho=I(15)/44 if s==-1 else ONE
    k=j*j;rl=B-L0;ru=B+L0;W=I(1)/32
    maxima=[ZERO,ZERO,ZERO]
    def divided(f,dr,dd):
        return [f/(rho*rl),(dr/rl+f/rl**2)/rho**2,(dd/rl+2*dr/rl**2+2*f/rl**3)/rho**3]
    for n in range(N+1):
        L=L0/(2**n)
        Q=factor*(cap['tail'] if n==N else cap['cell'][n])
        log=monotone_trans(1024/L**2,'ln')
        f=2*Q;dy=64*Q/L;fp=k*f/rl+dy
        w=8*L**3
        wp=8*(5*L**2+I(15)/4*B*L*log)
        pp=(10/L+I(15)/4*B*log/L**2)*dy
        U=ru*2*W*L**4*Q/(k-1);Up=w*fp;Upp=wp*fp+w*pp
        for d,(ad,ae) in enumerate(zip(divided(U,Up,Upp),divided(f,fp,pp))):
            val=upper((k-1)*ad/j+j*ae)
            if val.hi>maxima[d].hi:maxima[d]=val
    # For n>=N the successive factor Q shrinks by 1/32.  All terms are
    # positive sums of L^h, h>=-3, with at most one log(1024/L^2).
    # Its increase is <2 at the next cell. Every term therefore decreases.
    return dict(d_plus_e_orders=[str(v.hi) for v in maxima],old_cut_amplitude=factor.bounds(),last_cell=N,
                negative_cut_fpp=port['f_0_1_2'][2])


def omitted_sectors(coefficients,scales,cost,center):
    ans=[]
    # Exact binary parameter, multiplied by the same binary amplitude scale used by Layout.
    for ix,s in enumerate((-1,1)):
        a=[I(D.from_float(abs(float(coefficients[ix,j]*scales[ix,j])))) for j in range(2)]
        S=[sum((a[j]*I(cost[ix][j]['d_plus_e_orders'][i])/4 for j in range(2)),ZERO) for i in range(3)]
        fail=dict(available=False,side=s,raw_stereo_bounds=[str(t.hi) for t in S])
        if S[0].hi>D('.1'):ans.append(fail);continue
        d0=3*S[0];d1=4*S[1];d2=4*(S[2]+3*S[1]**2)
        P=8*(2+d0)*d0;P1=16*(1+d0)*d1;P2=16*((1+d0)*d2+d1**2)
        if P.hi>=D('.4'):ans.append(fail);continue
        lo=1-P;G=2*P1/lo;Gp=(P1+7*G*P)/lo;Gr=(2*P2+G*P1)/lo
        U=(4+P)*P;Ur=(4+2*P)*P1;Urr=(4+2*P)*P2+2*P1**2
        t=2*P/lo;tp=15*P/lo;du=Ur+G*(1+P)
        ddu=Urr+2*G*P1+G*G*(1+7*P)+(G*Gp+Gr)*(1+P)
        r0,r1=(I('.075'),I('.075')+I(15)/44*L0) if s==-1 else (B-L0,B)
        radial=U+r1*du;degree=radial+t;cr=radial+I('1.001')*t+radial*t
        if degree.hi>=D('.45') or cr.hi>=D('.45'):ans.append(fail);continue
        nr=2*cr/(1-cr)
        hrr=2*du+r1*ddu+I('4.4')*nr
        hrp=t/r0+2*P1/lo+G*(1+tp)+nr/r0
        hpp=(tp+P)/(r0*lo)+nr/r0
        kg=(I('4.4')+hrp+I(max(hrr.hi,hpp.hi)))/(1-degree)**2
        metric=2*I('1.001')*degree+degree**2
        cx=I(D.from_float(float(center[0]))) if s==-1 else ZERO
        cz=I(D.from_float(float(center[2]))) if s==-1 else ZERO
        # True auxiliary shift may change the material label. The complete
        # image has the same auxiliary-angle set; the reference point here uses that angle.
        pos=r1*U
        rho=r1+upper(cx)+pos+I('0.0000001')
        minus_z=(r1*I('.27')-cz if s==-1 else ZERO)+pos+I('.0000001')
        zmax=(cz+r1*I('.27') if s==-1 else ZERO)+pos+I('.0000001')
        h=minus_z-I('.045')
        side=rho+(I('2.914') if h.hi>=0 else I('2.9'))*h+I('.18492')
        ok=((3*kg).hi<D(100) and nr.hi<D('.2') and (rho+I('.06')).hi<D('.28499')
            and side.hi<D('.4215') and minus_z.hi<D('.075') and zmax.hi<D('.06'))
        ans.append(dict(available=bool(ok),side=s,raw_stereo_bounds=[str(v.hi) for v in S],
                   normalized_metric_operator_upper=str(metric.hi),principal_curvature_upper=str(kg.hi),
                   normal_displacement_upper=str(nr.hi),position_perturbation_upper=str(pos.hi),
                   material_speed_lower=str(lo.lo),max_radius_upper=str(rho.hi),
                   minimum_z_lower=str(-minus_z.hi),maximum_z_upper=str(zmax.hi),side_left_upper=str(side.hi)))
    return ans
