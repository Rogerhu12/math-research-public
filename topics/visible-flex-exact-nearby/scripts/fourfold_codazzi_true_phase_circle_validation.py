"""All-mode residual and true characteristic jets on a physical radial cell.

The input polynomial speeds are dimensionless in tau in [0,1]. Actual
periodic lifts stay real. Candidate coefficients and every retained endpoint
are exact binary dyadics. Rounding at a join is an explicit signed jump fee.
"""
from functools import lru_cache
from math import comb,factorial,isfinite
from flint import acb,arb
from fourfold_codazzi_signed_density_transport_arithmetic import LP
from fourfold_codazzi_true_characteristic_residual_transport import (
    initial_whole_circle,propagate,gap_source)
from fourfold_codazzi_true_phase_original_inputs import check

NMODES=128
TIME_DEGREE=6
JET_ORDER=9
GRID=2048


def point(z):
    x,y=float(z.real.mid()),float(z.imag.mid())
    check(isfinite(x) and isfinite(y),"finite candidate coefficients")
    return acb(arb(x),arb(y))


def dyadic(p):
    v=[acb(0)]*(2*NMODES+1)
    v[NMODES]=point(acb(p.coeff(0).real))
    for j in range(1,NMODES+1):
        z=point((p.coeff(j)+p.coeff(-j).conjugate())/2)
        v[NMODES+j]=z;v[NMODES-j]=z.conjugate()
    return LP(v,-NMODES)


@lru_cache(maxsize=4000)
def powers(k,order):
    return tuple((4*k)**m for m in range(order+1))


def norms(poly,order):
    """All supported modes of a whole interval LP in the physical variable."""
    v=[arb(0) for _ in range(order+1)]
    for i,z in enumerate(poly.p):
        if z.is_zero():continue
        a=abs(z).upper()
        for m,f in enumerate(powers(abs(poly.lo+i),order)):
            v[m]+=a*f
    return [(a/factorial(m)).upper() for m,a in enumerate(v)]


def polyval(v,x):
    p=LP()
    for c in reversed(v):
        p=p*x+c
    return p


def samples(p,m):
    a=[acb(0)]*GRID
    for k in range(p.lo,p.hi+1):
        a[k%GRID]+=p.coeff(k)*acb(0,4*k)**m/factorial(m)
    return [GRID*y for y in acb.dft(a,inverse=True)]


def fit(nodes):
    # The DFT values propose finite coefficients only. All actual aliases are
    # paid by an independent node and whole-bin residual check below.
    low=acb.dft(nodes[0]);high=acb.dft(nodes[JET_ORDER])
    a=[]
    for j in range(-NMODES,NMODES+1):
        z=low[j%GRID]/GRID if abs(j)<=4 else high[j%GRID]*factorial(JET_ORDER)/(GRID*acb(0,4*j)**JET_ORDER)
        a.append(z)
    return dyadic(LP(a,-NMODES))


def initial(seed,p,order):
    nodes,whole=seed
    half=arb.pi()/(4*GRID)
    noderr=[];highest=samples(p,order)
    for m in range(order):
        est=samples(p,m)
        noderr.append(max(abs(a-b).upper() for a,b in zip(nodes[m],est)))
    # Both the true field and its polynomial comparison refer to this same
    # centered angular bin. Evaluate the comparison there by the mean value
    # theorem, using its whole (order+1)st normalized jet.
    fee=(order+1)*half*norms(p,order+1)[-1]
    worst=max(abs(a-b).upper() for a,b in zip(whole[order],highest))+fee
    return initial_whole_circle(noderr,worst.upper(),half)


def reference(q0,vel):
    v=[q0];dq=[1+q0.d()]
    for k in range(TIME_DEGREE):
        # Only the point Taylor coefficients of the speed are used for this
        # proposal. The true last interval coefficient is reserved for proof.
        c=sum((vel[i]*dq[k-i] for i in range(min(k,len(vel)-2)+1)),LP())
        a=dyadic((-c)/(k+1));v.append(a);dq.append(a.d())
    return v


def residual(q,nominal,perturb,source=None):
    """Return the entire signed negative residual, without an angular cutoff.

    For phase source=None the equation is q_tau+vel(1+q_phi)=0.
    The supplied source, if present, is a full time polynomial on the RHS;
    then the equation is q_tau+vel*q_phi=source.
    """
    dq=[p.d() for p in q]
    if source is None:dq[0]=dq[0]+1
    n=max(len(q)-1,len(nominal)+len(q)-1,0 if source is None else len(source))
    r=[LP() for _ in range(n)]
    for k,p in enumerate(q[1:]):r[k]=r[k]-(k+1)*p
    if source is not None:
        for k,p in enumerate(source):r[k]=r[k]+p
    for i,a in enumerate(nominal):
        for j,u in enumerate(dq):r[i+j]=r[i+j]-a*u
    whole=arb(0).union(arb(1))
    return polyval(r,whole)-perturb*polyval(dq,whole)


def correlated_residual(qx,qw,d,b,dd,db):
    gx=[f.d() for f in qx];gx[0]=gx[0]+1
    src=[LP() for _ in range(len(b)+len(qx)-1)]
    for i,v in enumerate(b):
        for j,u in enumerate(gx):src[i+j]=src[i+j]+v*u
    # Combine b*qx_phi and -d*qw_phi by time power before supremum.
    one=arb(0).union(arb(1))
    return residual(qw,d,dd,src)+polyval(gx,one)*db


def averaged(a,b,sign):
    return [(x+sign*y)/2 for x,y in zip(a,b)]


def advance(starts,errors,speeds):
    d,b,dd,db,dwhole=speeds
    dw=norms(dwhole,JET_ORDER);S=dw[1]
    q=[];out=[];radial=[]
    for k,sign in enumerate((1,-1)):
        nom=[v+sign*w for v,w in zip(d,b)]
        trial=reference(starts[k],nom)
        forcing=norms(residual(trial,nom,dd+sign*db),JET_ORDER)
        out.append(propagate(arb(1),S,dw,errors[k],forcing));q.append(trial)
        vel=polyval(nom,arb(0).union(arb(1)))+dd+sign*db
        radial.append((forcing[0]+norms(vel,0)[0]*out[k][1]).upper())
    qx=averaged(q[0],q[1],1)
    qw=averaged(q[1],q[0],-1)
    n=JET_ORDER-1
    direct=norms(correlated_residual(qx,qw,d,b,dd,db),n)
    ballb=abs(polyval(b,arb(0).union(arb(1))).scalar()+db).upper()
    source=gap_source(direct,ballb,out[0],out[1])
    wc=propagate(arb(1),S,dw,errors[2],source)
    out.append([min(v,(p+m)/2).upper() for v,p,m in zip(wc,out[0],out[1])])
    endpoints=[polyval(v,arb(1)) for v in q]
    starts=[dyadic(v) for v in endpoints]
    joins=[a-b for a,b in zip(endpoints,starts)]
    join_norm=[norms(p,JET_ORDER) for p in joins]+[norms((joins[1]-joins[0])/2,n)]
    next_errors=[[(x+y).upper() for x,y in zip(v,w)] for v,w in zip(out,join_norm)]
    # The stored continuous comparison is q(tau)-tau*join, including its
    # true derivative correction. The PDE residual above is for q itself.
    radial=[(a+w[0]).upper() for a,w in zip(radial,join_norm)]
    return q,next_errors,starts,radial
