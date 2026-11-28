"""Complete original local G.7 data on closed root-to-cut r,phi boxes."""
from fractions import Fraction as Q
from math import factorial
from flint import arb,acb
import fourfold_codazzi_root_Laurent_Taylor_algebra as L
from fourfold_codazzi_true_characteristic_root_input import cauchy_tail,radial_laurent
from fourfold_codazzi_true_phase_original_inputs import check


def closed_bins(poly,tail,bins,width=0):
    """Full complex values, exact DFT alias sums plus real cell Taylor bound."""
    check(bins>=2 and not bins&(bins-1),"complete periodic partition")
    if width:
        poly=L.LP(poly.lo,[z*(-4*h*L.ex(width)).exp() for h,z in enumerate(poly.c,poly.lo)])
    values=[]
    for k in range(4):
        folded=[acb(0) for _ in range(bins)]
        for h,z in enumerate(poly.c,poly.lo):folded[h%bins]+=z
        values.append([bins*v for v in acb.dft(folded,inverse=True)])
        poly=poly.theta()
    half=arb.pi()/(4*bins);delta=arb(0,half.upper())
    excess=(tail+sum((abs(z) for z in poly.c),arb(0))*half**4/24).upper()
    error=acb(arb(0,excess),arb(0,excess));ans=[]
    for a,b,c,d in zip(*values):ans.append(a+delta*(b+delta*(c/2+delta*d/6))+error)
    return ans


def old_field(series,major,rho,bins,radial=0,angular=0,width=0):
    p=radial_laurent(series,rho,radial).theta(angular) if angular else radial_laurent(series,rho,radial)
    M,R,s=major;check(abs(width)<s,"strict signed angular strip loss")
    return closed_bins(p,cauchy_tail((M,R,s-abs(width)),abs(rho).upper(),len(series),radial,angular),bins,width)


def old_num(series,rho,tail_at_outer,outer,bins,width):
    # Each term in the saved positive tail has radial power at least eleven.
    # The old stored split gives this upper outright, without subtraction.
    error=tail_at_outer*(abs(rho).upper()/L.ex(outer))**len(series)
    return closed_bins(radial_laurent(series,rho,0),error,bins,width)


def real(z):
    check(z.imag.contains(0),"true real slice of the full signed old field")
    return z.real


def geometry(arr,oldmaj,raw,ntail,outer,rho,bins,width=0):
    columns={}
    for key in ('T','Xp','Q','a0','b0','w1a','w1b'):
        derivs=((0,0),(1,0),(0,1)) if key!='T' else ((0,0),(0,1),(0,2))
        for r,t in derivs:
            columns[key,r,t]=old_field(arr[key],oldmaj[key],rho,bins,r,t,width)
    for key in ('d','T0','vq','fb','fa','chi'):
        columns[key,0,0]=old_field(arr[key],oldmaj[key],rho,bins,width=width)
    for key in ('Nraw_a','Nraw_b'):
        columns[key,0,0]=old_num(raw[key],rho,ntail[key],outer,bins,width)
    for i in range(bins):
        val=lambda k,r=0,t=0:columns[k,r,t][i]
        slice_value=(lambda z:z) if width else real
        T,x,q,d,t0,vq=map(slice_value,[val(k) for k in ('T','Xp','Q','d','T0','vq')]);y=slice_value(val('T',0,1))
        mu=q*q*(x*x+T*y*y)
        check(abs(mu).lower()>0 and abs(x).lower()>0 and abs(q).lower()>0,"true signed root phase determinant")
        D=lambda k:-val(k,1,0)-d*val(k,0,1)
        at=slice_value(D('Q')*x+q*D('Xp')+q*q*T*val('T',0,2))-t0*q*x
        Dt=lambda k:q*(x*D(k)+q*T*y*val(k,0,1))
        # Undo the normalized [a0,Tb0;b0,a0]^{-1} which was used in the old
        # fb,fa stages.  -mu times the resulting original F is A0(w0).
        a,b=val('a0'),val('b0');fb,fa=val('fb'),val('fa')
        A0=(-mu*(a*fb+T*b*fa),-mu*(b*fb+a*fa))
        yield dict(chi=slice_value(val('chi')),T=T,x=x,y=y,q=q,mu=mu,at=at,vq=vq,w0=(a,b),w1=(val('w1a'),val('w1b')),
                   dw0=(Dt('a0'),Dt('b0')),dw1=(Dt('w1a'),Dt('w1b')),A0=A0,
                   N=(val('Nraw_a'),val('Nraw_b')))


def joint(g,invn,V,Vt,B,Bt,Btt,eps):
    """Direct original signed entries; GFW.4 and G.6 share mu,T,x,y and V."""
    T,x,y,q,mu,at,vq=(g[k] for k in ('T','x','y','q','mu','at','vq'))
    a,b=g['w0'];b*=eps
    a1,b1=g['w1'];a1*=eps
    da,db=g['dw0'];db*=eps
    da1,db1=g['dw1'];da1*=eps
    f1,f2=g['A0'];f2*=eps
    na,nb=g['N'];na*=eps
    ca=a1+B*T*b;cb=b1+B*a
    h=mu*Btt+at*Bt
    L1=(na+B*T*f2-mu*V*ca-2*Bt*T*db-h*T*b-mu*Bt*b,
        nb+B*f1-mu*V*cb+2*Bt*da+h*a)
    # Only the second component enters E12; D_T K w0 in that component is da.
    dcb=db1+B*da+mu*Bt*a
    cfirst=2*V*dcb+(mu*Vt+at*V)*cb
    gap=x*x+T*y*y-y*y*V*invn*invn;check(abs(gap).lower()>0,"complete signed G.5 gap")
    ii=acb(0,eps)
    def rank(a,b):
        v=-vq*V*(ii*y*a+x*b)/gap
        return ii*x*v,-y*v
    r0=rank(a,b);r1=rank(ca,cb)
    total=(L1[0]+(r0[0]-cfirst)*invn+r1[0]*invn*invn,L1[1]+r0[1]*invn+r1[1]*invn*invn)
    return total
