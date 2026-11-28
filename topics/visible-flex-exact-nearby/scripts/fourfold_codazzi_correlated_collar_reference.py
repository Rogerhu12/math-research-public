"""Signed root-collar reference Green matrix on the original two input columns.

All series coordinates are t=T/R.  The second row of a propagated vector
is R*Y_T.  The two zero-anchored responses are accumulated by their own
inhomogeneous equations before any norm or real absolute value is taken.
"""
from fractions import Fraction as Q
from flint import arb, acb
import fourfold_codazzi_common_radial_potential_budget as P
from fourfold_codazzi_true_phase_original_inputs import check

R=Q(1,32768)
L=Q(1,2000)
NMAX=4*(2**20+1)
ORDER=64
POT_ORDER=12


def actual_real(z):
    # These scalar jets are involution-real on the selected real family.
    z=acb(z)
    check(z.is_finite() and z.imag.contains(0),"real original reference coefficient")
    return z.real


def rho_to_t(poly,bart):
    """True radial reversion: poly(rho)=sum_j out[j]*(bart(rho)/R)^j."""
    n=len(poly)
    check(len(bart)>=n and bart[0]==0 and not bart[1].contains(0),"simple unshifted radial reference root")
    scaled=[v/P.ex(R) for v in bart[:n]]
    powers=[P.jconst(1,n)]
    for _ in range(1,n):powers.append(P.jmul(powers[-1],scaled,n))
    out=[]
    for k,pk in enumerate(poly):
        tail=sum((out[j]*powers[j][k] for j in range(k)),acb(0))
        out.append((pk-tail)/powers[k][k])
    return [actual_real(v) for v in out]


def scaled_potential(c,jlo,jhi):
    """Same radial original potential on this explicit positive real z band."""
    check(jlo>=97 and (jhi is None or jlo<=jhi),"actual original carrier band")
    count=POT_ORDER+3
    z=acb((arb(0) if jhi is None else P.ex(Q(1,jhi*jhi))).union(P.ex(Q(1,jlo*jlo))))
    plain={key:[p.scalar_value() for p in c[key][:count]] for key in ("K","beta","gamma","s","eta","k","a")}
    check(plain["K"][0]==0 and all(len(row)==count for row in plain.values()),"saved scalar jets on true root")
    data={"intrinsic":plain,"eta":plain["eta"]}
    for name in ("u","v"):
        check(len(c[name])>=count,"complete actual background through needed degree")
        data[name]={j:[p.coefficient(j) for p in c[name][:count]] for j in range(-96,97)}
    fields=P.full_frequency_fields(data,z,count)
    abar=[a*P.ex(Q(3,2*i+3)) for i,a in enumerate(plain["a"])]
    rr=lambda row:[-v for v in P.jdr(row)]
    d=count-1
    er=P.jdiv(rr(plain["eta"]),plain["eta"],d)
    kr=P.jdiv(rr(plain["k"]),plain["k"],d)
    ar=P.jdiv(rr(abar),abar,d)
    theta=fields["theta"]
    zr=P.jdiv(rr(theta),P.jadd(P.jconst(1,count),theta,count),d)
    cc=[kr[i]/4-ar[i]/6-fields["D"][i]/2-zr[i]/2 for i in range(d)]
    ellq=[2*er[i]+kr[i]/2-ar[i]/3+fields["D"][i]+zr[i] for i in range(d)]
    m=count-2
    cross=P.jmul(cc,ellq,m);aa=fields["alpha"]
    freq=P.jadd(P.jscale(P.jmul(plain["eta"],aa,m),2),P.jscale(P.jmul(aa,aa,m),z),m)
    kfreq=P.jmul(plain["K"],freq,m)
    W=[-v+cross[i]/2-16*kfreq[i] for i,v in enumerate(rr(cc))]
    kappa=P.jmul(plain["a"],P.jpow(abar,Q(-1,3),m),m)
    pot=P.jdiv(W,P.jmul(kappa,kappa,m),m)
    bart=[acb(0)]+[-a for a in P.jpow(abar,Q(2,3),m-1)]
    return rho_to_t(pot,bart)


def bounded_potential(coeff,count):
    """All coefficients of V(Rt), including honest original holomorphic tails."""
    rr=P.ex(R/L)
    out=[]
    for k in range(count):
        lim=276*P.ipow(rr,k)
        cap=arb(0,lim.upper())
        if k<len(coeff):
            check(coeff[k].overlaps(cap),"signed radial coefficient and original complex disk bound")
            out.append(coeff[k].intersection(cap))
        else:out.append(cap)
    return out


def conv(a,b,k):
    return sum((a[h]*b[k-h] for h in range(k+1)),arb(0))


def jets(coeff,jlo,jhi,order=ORDER):
    """Canonical V/free matrices, signed V-minus-free and WUA.54 Green integral.

    Returned columns use identical (Y(0),R Y_T(0)) before the physical
    right matrix diag(1,R) F_n(0) C_n or its declared free analogue.
    The root mismatch carried by D_root is distinct from the Green integral.
    """
    check(97<=jlo<=jhi<=NMAX//4 and order>=4,"entire scaled collar domain")
    n=arb(4*jlo).union(arb(4*jhi));scale=P.ex(R)
    q=n*n*scale*scale*scale
    check(q.upper()+276*scale*scale<1,"canonical disk generator at most one")
    v=bounded_potential(coeff,order+2)
    b=[x/(2*h+1) for h,x in enumerate(v)]
    h=[(k+1)*(k+2)*b[k+2]/(scale*scale)+conv(v,b,k) for k in range(order)]
    cols=[]
    for initial in ((1,0),(0,1)):
        f=list(map(arb,initial));dv=[arb(0),arb(0)];green=[arb(0),arb(0)]
        for k in range(order-1):
            a=(k+1)*(k+2);lag=lambda row:row[k-1] if k else arb(0)
            f.append(q*lag(f)/a)
            dv.append((q*lag(dv)-scale*scale*(conv(v,f,k)+conv(v,dv,k)))/a)
            # R^2*(H/n^2)*Y_T^free = (R/n^2)*H*(d_t Y^free).
            forcing=sum((h[u]*(k-u+1)*f[k-u+1] for u in range(k+1)),arb(0))
            green.append((q*lag(green)-scale*scale*conv(v,green,k)+scale*forcing/(n*n))/a)
        cols.append({"free":f,"genuine_minus_free":dv,"darboux_green":green})
    return cols


def evaluation(matrix,t,jlo):
    """Value and t-derivative enclosures with uniform complete analytic tails."""
    u=abs(t).upper();check(u<P.ex(Q(3,5)),"genuine true collar within scaled disk")
    nmin=4*jlo;scale=P.ex(R)
    # Circle bounds follow by integrating along the straight complex radius.
    # On the radius R, |B''|<=3830956/5 since V has the old complete V''
    # bound throughout |T|<=L. Both free and perturbed generators have norm <=1.
    radii={"free":arb(3),"genuine_minus_free":9*scale*scale*276,
           "darboux_green":9*scale*(arb(3830956)/5+276*276)/(nmin*nmin)}
    out=[]
    for col in matrix:
        piece={}
        for name,cs in col.items():
            first=len(cs);rad=radii[name]
            a=cs[-1];d=arb(0)
            for val in reversed(cs[:-1]):d=d*t+a;a=a*t+val
            e=rad*P.ipow(u,first)/(1-u)
            ed=rad*P.ipow(u,first-1)*(first/(1-u)+u/(1-u)**2)
            piece[name]=[a+inflate(t,e),d+inflate(t,ed)]
        out.append(piece)
    return out


def potential_values(coeff,t):
    """Signed V,V_T,B,B_T,B_TT on the same original t interval."""
    scale=P.ex(R);u=abs(t).upper();check(u<P.ex(Q(3,5)),"complete true reference collar")
    def terms(bfun,der):
        from math import factorial
        q=len(coeff);z=arb(0)
        for k in range(q-1,der-1,-1):
            f=factorial(k)//factorial(k-der);z=z*t+coeff[k]*f/(2*k+1 if bfun else 1)
        # For k>=q the ratio of adjacent absolute Cauchy summands is <=
        # (R/L)*u*(q+1)/(q+1-der); the extra B denominator only decreases it.
        ratio=P.ex(R/L)*u*(q+1)/(q+1-der)
        first=276*P.ipow(P.ex(R/L),q)*P.ipow(u,q-der)*(factorial(q)//factorial(q-der))
        if bfun:first/=2*q+1
        check(ratio<1,"infinite differentiated true-potential tail")
        return (z+inflate(t,first/(1-ratio)))/P.ipow(scale,der)
    return terms(False,0),terms(False,1),terms(True,0),terms(True,1),terms(True,2)


def inflate(like,rad):
    h=arb(0,rad.upper())
    return acb(h,h) if isinstance(like,acb) else h
