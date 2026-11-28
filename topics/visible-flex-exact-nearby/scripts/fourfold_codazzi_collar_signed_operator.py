"""Contour Fourier coefficients of the full signed G.8 local density.

The direct sum is over the physical 4j basis.  Both independent input
columns share the true right root shear before all physical multipliers.
"""
from math import isfinite,nextafter,inf
import struct
from fractions import Fraction as Q
from flint import acb,arb
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_phase_original_inputs import check
import fourfold_codazzi_correlated_collar_reference as F
import fourfold_codazzi_collar_signed_geometry as G

WIDTH=Q(1,512)
HARM=3072


def upper(x):
    v=nextafter(float(x.upper()),inf);check(isfinite(v) and v>=0,'finite complete nonnegative bound');return v


def root_frame(lo,hi):
    n=arb(4*lo).union(arb(4*hi));lam=(n.log()*2/3).exp();s=arb(3).sqrt()
    a=1/((arb(3).log()*2/3).exp()*exact(Q(2,3)).gamma())
    d=-1/((arb(3).log()/3).exp()*exact(Q(1,3)).gamma());r=exact(F.R)*lam
    beta=arb(0,(100/(arb(4*lo).log()*4/3).exp()).upper())
    # The whole old terminal-Ai shear bound is valid for both signs; beta
    # only multiplies the second common column after each signed difference.
    return (a,r*d),(s*a,-r*s*d),beta


def append_box(sink,z):
    w=acb(z);v=[]
    for x in (w.real,w.imag):v.extend((nextafter(float(x.lower()),-inf),nextafter(float(x.upper()),inf)))
    check(all(isfinite(x) for x in v),'finite whole signed complex rectangle')
    sink.extend(struct.pack('<dddd',*v))


def symbols(gs,co,mat,lo,hi,sign,sink):
    inv=exact(Q(1,4*hi)).union(exact(Q(1,4*lo)));n=arb(4*lo).union(arb(4*hi))
    columns=root_frame(lo,hi);vals=[[],[]];ma=[arb(0),arb(0)];gr=arb(0)
    for g in gs:
        t=g['T']/exact(F.R);pot=F.potential_values(co,t);A,B=G.joint(g,inv,*pot,sign)
        ma=[max(ma[0],abs(A).upper()),max(ma[1],abs(B).upper())];xi=F.evaluation(mat,t,lo)
        z=[]
        for col in xi:
            free,dv=col['free'],col['genuine_minus_free']
            u=A*(free[0]+dv[0])+B*(free[1]+dv[1])*(inv/exact(F.R))
            z.append(u)
            gr=max(gr,*(abs(v).upper() for v in col['darboux_green']))
        a,b=columns[0];c,d=columns[1];right=z[0]*c+z[1]*d
        left=z[0]*a+z[1]*b+columns[2]*right
        phase=(acb(0,sign)*n*g['chi']).exp()
        vals[0].append(left*phase);vals[1].append(right*phase)
        # Natural contour packet uses the same actual field T and its full
        # potential, two signed amplitudes, phase, two root columns and
        # every scaled entry of the free, genuine and anchored Green frame.
        fields=[g['T'],*pot,A,B,phase,vals[0][-1],vals[1][-1]]
        for col in xi:
            for key in ('free','genuine_minus_free','darboux_green'):fields.extend(col[key])
        for field in fields:append_box(sink,field)
    return vals,ma,gr


def fourier(values):
    N=len(values);centres=[acb(p.real.mid(),p.imag.mid()) for p in values]
    error=sum((abs(z-c).upper() for z,c in zip(values,centres)),arb(0))/N
    return [z/N for z in acb.dft(centres)],error.upper(),max(abs(v).upper() for v in values)


def lag_weights(lo,hi,h,sign):
    # sign is the original input sign and h is a signed envelope lag.
    low,high=(lo+h,hi+h) if sign==1 else (-hi+h,-lo+h)
    m=0 if low<=0<=high else min(abs(low),abs(high))
    return (arb(1+16*m*m).log()*exact(Q(-5,6))).exp()


def band_bound(gs,co,lo,hi,N,sink):
    mat=F.jets(co,lo,hi);density=(arb(4*hi).log()/6+arb(1+16*hi*hi).log()*exact(Q(2,3))).exp()
    decay=(-4*exact(WIDTH)).exp();ma=[arb(0),arb(0)];gr=arb(0)
    lags={};tail={};sinc=[arb(1)]+[(arb.pi()*h/N).sin()/(arb.pi()*h/N) for h in range(1,HARM+1)]
    for sign in (1,-1):
        sf={}
        for width in (WIDTH,-WIDTH):
            val,m,v=symbols(gs[width],co,mat,lo,hi,sign,sink)
            ma=[max(a,b) for a,b in zip(ma,m)];gr=max(gr,v)
            sf[width]=[fourier(a) for a in val]
        rows=[]
        for o in (-1,1):
            coeff=sf[-o*WIDTH];dn=arb(1);pr=[]
            for h in range(HARM+1):
                a=[]
                for cn,er,m in coeff:
                    approx=abs(cn[(o*h)%N]*sinc[h]).upper()+er
                    a.append(min(m,approx).upper()*dn)
                mag=(a[0]*a[0]+a[1]*a[1]).sqrt().upper()
                pr.append((mag*lag_weights(lo,hi,o*h,sign)).upper());dn*=decay
            rows.append(pr)
        lags[sign]=rows
        caps=[]
        for o in (-1,1):
            caps.append(sum((r[2]*r[2] for r in sf[-o*WIDTH]),arb(0)).sqrt())
        # Retain the stronger physical output derivative gain until h>=lo/2.
        h0=HARM+1;h1=max(h0,(lo+1)//2)
        weights=(decay**h0)*(arb(1+4*lo*lo).log()*exact(Q(-5,6))).exp() if h1>h0 else arb(0)
        tail[sign]=[(c*(weights+decay**h1)/(1-decay)).upper() for c in caps]
    # One l2 input space includes both signs and both reference columns. The
    # pointwise largest row is taken for each lag before the shift's unit norm.
    val=min(max(lags[1][a][0],lags[-1][a][0]) for a in (0,1))
    for a in (0,1):
        val+=sum((max(lags[1][a][h],lags[-1][a][h]) for h in range(1,HARM+1)),arb(0))
        # Each separate-sign tail above bounds a sum of all its lags. Their
        # sum bounds the sign-wise supremum without changing an infinite sum.
        val+=tail[1][a]+tail[-1][a]
    cost=(val*density).upper()
    return cost,dict(signed_amplitude_upper=list(map(upper,ma)),canonical_darboux_green_upper=upper(gr),
                     complete_original_density_Hminus5over3_upper=upper(cost))
