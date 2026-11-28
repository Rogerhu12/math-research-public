"""R755 normalized vector-area, boundary energy, and curvature collar witnesses, in directed intervals."""
from itertools import permutations
import numpy as np
from r734_true_dyadic_tail import I,D,ONE,ZERO,monotone_trans


CAP_SIN=I('.26999999999999','.27000000000001')


def cap_identity(theta,s_literal,c_literal):
    # Exact binary angle as a real angle. A Taylor remainder controls its mathematical sine.
    t=exact(theta);v=t;term=t
    for k in range(1,9):
        term=-term*t*t/((2*k)*(2*k+1));v+=term
    rem=I((term*t*t/(18*19)).norm());bounded=v+I(rem.hi.copy_negate(),rem.hi)
    c=sqroot(1-square(CAP_SIN));s0,c0=exact(s_literal),exact(c_literal)
    if not (CAP_SIN.lo<=bounded.lo and bounded.hi<=CAP_SIN.hi and CAP_SIN.lo<=s0.lo<=CAP_SIN.hi and c.lo<=c0.lo<=c.hi):
        raise ArithmeticError('Actual cap does not fall in the declared common hull.')
    return dict(exact_prescribed_sine='0.27',mathematical_sine_of_literal_angle=bounded.bounds(),
         literal_sine=s0.bounds(),literal_cosine=c0.bounds(),literal_orthonormality_discrepancy=(square(s0)+square(c0)-1).bounds(),
         all_tested_proper_rotations_sine_hull=CAP_SIN.bounds(),nonorthogonal_IEEE_matrix_is_not_an_exact_rotation=True)


def exact(x):return I(D.from_float(float(x)))
def square(x):
    x=I(x)
    lo=I(x.distance_from_zero())**2;hi=I(x.norm())**2
    return I(lo.lo,hi.hi)
def positive(x):return I(max(D(0),x.lo),max(D(0),x.hi))
def ab(x):return I(x.distance_from_zero(),x.norm())
def sqroot(x):
    z=monotone_trans(I(max(x.lo,D(0)),x.hi),'sqrt')
    return I(max(D(0),z.lo),z.hi)
def dot(x,y):return sum((a*b for a,b in zip(x,y)),ZERO)
def sh(x):
    return (monotone_trans(x,'exp')-monotone_trans(-x,'exp'))/2
def ch(x):
    return (monotone_trans(x,'exp')+monotone_trans(-x,'exp'))/2
def vup(x):return I(max(t.hi for t in x))
def mid(x):return (float(x.lo)+float(x.hi))/2
def ramp(r,center):
    y=r-I(center);h=I('.0025')
    if y.hi<=-h.lo:return ZERO
    if y.lo>=h.hi:return y
    t=I(max(D(-1),(y/h).lo),min(D(1),(y/h).hi))
    a=t-t**3+t**5*3/5-t**7/7+I(16)/35
    b=t**2/2-t**4*3/4+t**6/2-t**8/8-ONE/8
    return I(35)/32*(y*a-h*b)


def material_cell(lo,hi,M):
    """Only new work. M is the literal already-paid calibration; slopes use the original geometry."""
    lo,hi=I(lo),I(hi);r=I(lo.lo,hi.hi);w=hi-lo
    if r.hi<D('.08499999999999') or r.lo>D('.21000000000001'):p=ZERO
    else:
        center=(lo+hi)/2
        peak=ramp(center,'.0875')-2*ramp(center,'.1475')+ramp(center,'.2075')
        # Original bump is the convolution of a nonnegative triangle with a mass-one kernel.
        # Its global Lipschitz constant is one. Allow the original literal operations as well.
        err=w/2+I('1e-12');p=I(max(D(0),(peak-err).lo),(peak+err).hi)*I('2.01')*M
    tail=ZERO
    for side,hit in ((-1,r.lo<=D('.08500000000001')),(1,r.hi>=D('.20999999999999'))):
        if not hit:continue
        rho=I(15)/44 if side==-1 else ONE
        edge=I(1)/(64 if side==-1 else 128)
        dmax=I('.010000000001')/rho
        slope=I(max((8*edge**3).hi,(dmax**4/2).hi))
        # All old Gauss weights are positive, normalized up to the stated floating margin.
        # The physical cutoff height is everywhere bounded by the finite positive quadrature
        # on the deep cells plus the explicit quartic primitive on the flat transition.
        height=rho*(8*edge**4+I('.1')*dmax**5)*I('1.000000001')
        d=slope+I('938')*height+I('1e-12')
        tail=I(0,max(tail.hi,d.hi))
    m=sqroot(1+square(p)+square(tail))
    # 1e-12 covers residual binary multiplication/square-root roundoff, admitting E>=1.
    m=I(max(D(1),(m-I('1e-12')).lo),(m+I('1e-12')).hi)
    return tuple(q.bounds() for q in ((hi**2-lo**2)*m,monotone_trans(hi/lo,'ln')*m,w*m))


def matrix(A,L,C):
    a,b=I('.075'),I('.22');s=CAP_SIN;c=sqroot(1-s*s)
    Di=((c,ZERO),(ZERO,ONE),(-s,ZERO));Do=((ONE,ZERO),(ZERO,ONE),(ZERO,ZERO))
    B=[-a*a*s,ZERO,b*b-a*a*c]
    M=[]
    for i in range(3):
        M.append([2*C[i]*C[j]/L+(a*a*dot(Di[i],Di[j])+b*b*dot(Do[i],Do[j]))*ch(L)/sh(L)
            -a*b*(dot(Di[i],Do[j])+dot(Do[i],Di[j]))/sh(L) for j in range(3)])
    A4=[[M[i][j]/A for j in range(3)]+[B[i]/A] for i in range(3)]+[[b0/A for b0 in B]+[ZERO]]
    gap=[[(A if i==j else ZERO)-M[i][j]-B[i]*B[j]/A for j in range(3)] for i in range(3)]
    return A4,gap,B,Di,Do


def det(H):
    n=len(H);v=ZERO
    for p in permutations(range(n)):
        t=ONE
        for i,j in enumerate(p):t*=H[i][j]
        v+=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))*t
    return v


def quadratic(Q,v):return sum((v[i]*v[j]*a for i,row in enumerate(Q) for j,a in enumerate(row)),ZERO)
def selector(Q,largest):
    # Only chooses an exact binary test direction; the proof never uses an unenclosed eigenvalue.
    _,U=np.linalg.eigh([[mid(e) for e in row] for row in Q])
    return [exact(y) for y in U[:,-1 if largest else 0]]


def test_matrix(A,L,C):
    full,gap,B,Di,Do=matrix(A,L,C);q=selector(full,True)
    lam=quadratic(full,q)/sum((square(v) for v in q),ZERO)
    minors=[det([row[:n] for row in gap[:n]]) for n in range(1,4)]
    return dict(eta_Rayleigh_lower=str(max(D(0),(lam-1).lo)),Rayleigh_interval=lam.bounds(),
                actual_binary_test4=[v.bounds() for v in q],strictly_excluded=bool(lam.lo>1),
                gap_principal_leading_minors=[z.bounds() for z in minors],
                strict_PSD_gate_passed=bool(all(u.lo>0 for u in minors)),
                area_only_self_suffices=False),gap,B,Di,Do


def cap_cell(cell,A,L,C,B,Di,Do,v,Mc):
    """Each cell stores an area/π integral and two enclosing conformal/meridian prefixes."""
    r,area,x,di,do=cell
    nv=sqroot(sum((square(t) for t in v),ZERO))
    theta_s=CAP_SIN;theta_c=sqroot(1-square(theta_s))
    vdi=[dot(v,[row[j] for row in Di]) for j in range(2)]
    vdo=[dot(v,[row[j] for row in Do]) for j in range(2)]
    # L−x is nonnegative for every actual radius, even when independent interval arithmetic overlaps.
    x=I(max(D(0),x.lo),min(L.hi,x.hi))
    z=L-x;z=I(max(D(0),z.lo),z.hi)
    hs=[(I('.22')*ch(x)*d-I('.075')*ch(z)*e)/(r*sh(L)) for d,e in zip(vdo,vdi)]
    zero=-dot(v,C)/(L*r);mean_n=dot(v,B)/A
    n=[];y=[]
    for dist,ne,ve in ((di,theta_s*v[0]+theta_c*v[2],vdi),(do,v[2],vdo)):
        n.append(positive(ab(ne-mean_n)-Mc*dist*nv))
        rms=sqroot(square(zero)+sum((square(s-t) for s,t in zip(hs,ve)),ZERO)/2)
        y.append(positive(rms-Mc*dist*nv))
    # A lower bound uses max of the TWO genuine lower endpoints, not upper endpoints.
    nl=I(max(q.lo for q in n));yl=I(max(q.lo for q in y))
    return I(area.lo)*(square(nl)+square(yl))

