"""Complete physical-angle and invariant-label enclosures for the true first ratio.

Fourier aliases add with their actual signs. The angular continuation uses
Taylor's theorem on the full real bin. Invariant labels are treated on the
original lift; only their bounded periodic derivative data are indexed modulo.
"""
from math import comb,factorial,isfinite
from functools import lru_cache
from fractions import Fraction
import struct
from flint import acb,arb,arb_series
from fourfold_codazzi_signed_density_transport_arithmetic import LP,exact
from fourfold_codazzi_true_phase_original_inputs import check

# Each bin is a closed interval centered at 2*pi*j/(4*cells).
CELLS=128
M=6


def stream_row(f,head):
    """Decode GPR's seven radial powers and its separately stored endpoint."""
    H=head["positive_modes"];K=head["time_degree"];J=head["jet_order"]
    pair=struct.Struct("<dd");one=struct.Struct("<d")
    count=2*(K+2)*(H+1)
    raw=f.read(count*pair.size+(3*J+2)*one.size)
    check(len(raw)==count*pair.size+(3*J+2)*one.size,"whole GPR natural physical row")
    itr=iter(pair.iter_unpack(raw[:count*pair.size]));rows=[]
    for branch in range(2):
        v=[]
        for k in range(K+2):
            p=[acb(0)]*(2*H+1)
            for j in range(H+1):
                re,im=next(itr)
                check(isfinite(re) and isfinite(im) and (j!=0 or im==0),"Hermitian GPR coefficient")
                z=acb(arb(re),arb(im));p[H+j]=z;p[H-j]=z.conjugate()
            v.append(LP(p,-H))
        end=v.pop()
        # Exact continuous comparison on this cell.
        v[1]=v[1]+end-sum(v,LP())
        rows.append(v)
    err=[arb(e) for e, in one.iter_unpack(raw[count*pair.size:])]
    check(all(e.is_finite() and e>=0 for e in err),"all actual GPR jet upper bounds")
    return rows,[err[:J+1],err[J+1:2*J+2],err[2*J+2:]],raw


@lru_cache(maxsize=30000)
def angular_weight(j,m):
    return acb(0,4*j)**m/factorial(m)


def mesh(poly,order,err=None,cells=CELLS):
    """Normalized derivatives on the whole physical bins, including all aliases."""
    if err is None:err=[arb(0)]*(order+1)
    check(len(err)>order,"all actual unknown derivative errors")
    n=order+3;dft=[]
    for m in range(n+1):
        folded=[acb(0)]*cells
        for j,z in enumerate(poly.p,poly.lo):
            folded[j%cells]+=z*angular_weight(j,m)
        values=acb.dft(folded,inverse=True)
        check(all(z.imag.contains(0) for z in values),"complete real Fourier quantity")
        dft.append([cells*z.real for z in values])
    h=arb.pi()/(4*cells);angle=arb(0,h.upper())
    last=(sum((abs(z).upper()*abs(4*j)**(n+1) for j,z in enumerate(poly.p,poly.lo)),arb(0))
          /factorial(n+1)).upper()
    out=[]
    for k in range(cells):
        jets=[]
        for m in range(order+1):
            v=dft[n][k]*comb(n,m)
            for j in range(n-1,m-1,-1):
                v=v*angle+comb(j,m)*dft[j][k]
            fee=(err[m]+comb(n+1,m)*last*h**(n+1-m)).upper()
            jets.append(v+arb(0,fee))
        out.append(jets)
    return out


def geometry(rows,err,tau):
    def val(v):
        p=LP()
        for z in reversed(v):p=p*tau+z
        return p
    # Correlate the two exact trial polynomials BEFORE enclosing tau or phi.
    xdisp=val([(a+b)/2 for a,b in zip(*rows)])
    gap=val([(b-a)/2 for a,b in zip(*rows)])
    xd_err=[(a+b)/2 for a,b in zip(err[0],err[1])]
    x=mesh(xdisp,M+2,xd_err);w=mesh(gap,M+2,err[2])
    # Keep the available independent whole positive-branch GPR enclosure.
    u=mesh(val(rows[0]),M+2,err[0])
    return x,w,u


def series(a,n=None):
    n=len(a) if n is None else n
    check(len(a)>=n>0,"qualified normalized physical-angle jet")
    return arb_series(list(a[:n]),prec=n)


def derivative(a):
    return [(j+1)*v for j,v in enumerate(a[1:])]


def label_jet(a,p):
    """Normalize (p^-1 partial_phi)^m a/m! at the very same physical point."""
    v=series(a,M+1);p=series(p,M+1)
    check(p[0].lower()>0,"true monotone physical root label")
    out=[v[0]];ip=1/p
    for k in range(1,M+1):
        n=M+1-k
        v=series([(j+1)*v[j+1] for j in range(n)])*ip/k
        out.append(v[0])
    return out


def angular_compose(a,P):
    """Normalized jet of a label function pulled back by its true phase."""
    delta=series([arb(0),*P[1:M+1]])
    v=series([a[M]]+[arb(0)]*M)
    for j in range(M-1,-1,-1):v=v*delta+a[j]
    check(v.prec>=M+1,"whole composition order")
    return [v[j] for j in range(M+1)]


def label_bins(physical_index,displacement):
    """Every label bin intersecting the lifted image of this closed physical bin."""
    # phi in bin i -> M*phi/period in i+[-1/2,1/2]; add +/-1/2
    # for the label target width itself. No rounded circular lift selected.
    lo=arb(physical_index-1)+2*CELLS*displacement.lower()/arb.pi()
    hi=arb(physical_index+1)+2*CELLS*displacement.upper()/arb.pi()
    start=int(lo.lower().ceil().fmpz());end=int(hi.upper().floor().fmpz())
    check(start<=end,"nonempty lifted exact label image")
    return tuple(range(CELLS)) if end-start+1>=CELLS else tuple(j%CELLS for j in range(start,end+1))


def project_to_labels(images,physical):
    out=[None]*CELLS
    for ids,v in zip(images,physical):
        for j in ids:
            out[j]=list(v) if out[j] is None else [a.union(b) for a,b in zip(out[j],v)]
    check(all(v is not None for v in out),"the actual monotone circle covers every label")
    return out


def project_to_physical(images,labels):
    out=[]
    for ids in images:
        v=list(labels[ids[0]])
        for j in ids[1:]:v=[a.union(b) for a,b in zip(v,labels[j])]
        out.append(v)
    return out
