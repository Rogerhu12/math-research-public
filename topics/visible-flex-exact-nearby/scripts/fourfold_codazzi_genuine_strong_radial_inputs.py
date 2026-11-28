"""One-sided signed inward radial jets for the free first-amplitude wave.

The background uses the 65 original cubic coordinates, the independent
mean, the 193-coordinate repaired direction and the whole native scalar
Taylor models on the original cell. Orders are explicitly restricted
before any mixed-degree product. No radial derivative of an enclosure
is taken, and an artificial split never moves a genuine junction.
"""
from fractions import Fraction
from math import comb
from flint import arb
from fourfold_codazzi_signed_density_transport_arithmetic import Jet,LP,exact,hull
from fourfold_codazzi_true_phase_original_inputs import CONTROL,DELTA,check
from fourfold_codazzi_true_phase_signed_speed import restricted


def take(v,n):
    check(0<n<=v.n,"all requested true radial Taylor coefficients")
    return Jet(v.c[:n])


def inward(v):
    return Jet([(-1)**j*a for j,a in enumerate(v.c)])


def cell_fields(inp,direction,kmodels,cell,left=None,right=None):
    """Normalized rho coefficients at each common point of the closed cell.

    K has order four. d,b,eta and beta*mean(S) have order three. The
    scalarization quantities T0,V0,theta have order two. Every angular
    coefficient is a complete finite Laurent polynomial, including the mean.
    """
    l,r,k,i=cell
    l=l if left is None else Fraction(left)
    r=r if right is None else Fraction(right)
    check(cell[0]<=l<=r<=cell[1],"original one-sided physical subcell")
    centre,models=inp.rows[i]
    t=hull(l-centre,r-centre);xc=hull(l-inp.nodes[k],r-inp.nodes[k])
    co=inp.piece(k);zu,zv,range_z=direction
    width=min(inp.nodes[k+1],range_z[1])-max(inp.nodes[k],range_z[0])
    check(width>0,"original maximal qualified direction cubic")
    fees=[None]+[exact(Fraction(m)/width**j) for j,m in enumerate((18,48,32),1)]

    def intrinsic(key,n):
        model=kmodels[i] if key=="K" else models[key]
        return Jet([restricted(model,t,j) for j in range(n)])

    def background(which,repair,perturb):
        out=[]
        for j in range(4):
            p=LP()
            for z in range(3,j-1,-1):
                p=p*xc+co[z][which]*comb(z,j)
            out.append(p+(repair if j==0 else perturb*fees[j]))
        return Jet(out)

    u=background(0,inp.du,zu)
    v=background(1,inp.dv,zv)+intrinsic("s",4)
    K=intrinsic("K",5);gamma=intrinsic("gamma",4)
    q=restricted(models["q"],t,0)
    check(q.lower()>0 and K.c[0].scalar().overlaps(-q*q),
          "native positive q and native K describe the same complete cell")
    K.c[0]=LP.const(K.c[0].scalar().intersection(-q*q))
    a,bb=CONTROL
    if cell[0]>=a and cell[1]<=bb:
        # Use six coefficients to obtain all five of w' on the true piece.
        unit=Jet([hull((l-a)/(bb-a),(r-a)/(bb-a)),exact(1/(bb-a)),0,0,0,0])
        w=4096*(unit*(1-unit))**6
        delta=arb(0,exact(DELTA))
        K=(-delta*take(w,5)).exp()*(K+delta*intrinsic("T",5)*w.derivative())
        gamma=gamma*(take(w,4)*(delta/2)).exp()
    check(K.c[0].scalar().upper()<0,"true negative curvature on whole strict cell")
    K3=take(K,4)
    eta=-gamma*v.mean()
    check(eta.c[0].scalar().lower()>0,"original independent mean and positive eta")
    beta=intrinsic("beta",4)
    b=eta*(-K3).sqrt()
    S=u*u+K3*v*v
    d=-beta*S.primitive()
    ell=-2*beta*u*v
    e=-beta*(1+3*u*u+K3*v*v)
    bloc=beta*(1-u*u-3*K3*v*v)
    # Tq, Rq and V0 contain physical outward r derivatives by definition.
    # Form every undifferentiated factor at the common order two first.
    eta2,d2,u2,v2,beta2,K2=[take(z,3) for z in (eta,d,u,v,beta,K3)]
    ell2,e2,bloc2=[take(z,3) for z in (ell,e,bloc)]
    mlog=eta.derivative()/eta2
    dphi=d2.dphi()
    tq=dphi+e2+mlog
    rq=(ell.derivative()-d2*ell2.dphi()+e2.dphi()*eta2
        -2*beta2*eta2*u2.dphi()*u2-ell2*(dphi+mlog))
    v0=tq*bloc2-bloc.derivative()+d2*bloc2.dphi()-(ell2*ell2-4*beta2*eta2*v2*u2.dphi())*K2
    theta=rq/eta2-2*beta2*K2*v2*v2.dphi()
    return {name:inward(z) for name,z in
            (("K",K),("d",d),("b",b),("eta",eta),("beta_mean_S",beta*S.mean()),
             ("T0",tq+bloc2),("V0",v0),("theta",theta))}
