"""A continuous backward trial and a directed flat-measure residual on the real negative body."""
from bisect import bisect_right
from fractions import Fraction
import hashlib
from pathlib import Path

import numpy as np
from flint import acb, arb

import fourfold_codazzi_fixed_negative_Newton_radial as m

N = 8
PROPOSAL_GRID = 512


def coefficients(field):
    p = np.zeros(PROPOSAL_GRID,dtype=np.complex128)
    if not isinstance(field,m.Laurent):
        p[0] = complex(float(acb(field).real.mid()),float(acb(field).imag.mid()))
    else:
        for k in range(-field.degree,field.degree+1):
            z = field.coeff(k)
            p[k] = complex(float(z.real.mid()),float(z.imag.mid()))
    return p


def select_trial(physical, half, right, bracket):
    """Uncertified choices only. Everything returned is subsequently treated as an exact dyadic."""
    if bracket:
        m.require(np.all(right==0),"the same exact zero on the complete uncertain root bracket")
        return np.zeros((N+1,m.DIM),dtype="<f8")
    cheb = np.polynomial.chebyshev
    pts = np.cos(np.arange(N+1)*np.pi/N)
    v = cheb.chebvander(pts,N)
    q = np.empty(v.shape)
    for i,cs in enumerate(np.linalg.inv(v).T):
        integ = cheb.chebint(cs)
        q[:,i] = cheb.chebval(pts,integ)-cheb.chebval(1,integ)
    def grid(field):
        return np.fft.ifft(coefficients(field)).real*PROPOSAL_GRID
    force = np.array([[grid(f) for f in src] for src,op in physical])
    d,a12,a21,l11,l12,l21,l22,u,kv,n1,n2,m1,m2 = (
        np.stack([grid(op[j]) for src,op in physical]) for j in range(13))
    deriv = (4j*np.fft.fftfreq(PROPOSAL_GRID)*PROPOSAL_GRID)[None,:]
    prim = np.zeros_like(deriv)
    prim[:,1:] = 1/deriv[:,1:]
    prim[:,PROPOSAL_GRID//2] = 0
    def packed(x,y):
        return np.concatenate((-np.sqrt(2)*x[:,1:m.HEAD+1].imag,y[:,0:1].real,
                               np.sqrt(2)*y[:,1:m.HEAD+1].real),axis=1)
    def bwd(z):
        return np.fft.ifft(z,axis=1).real*PROPOSAL_GRID
    def fwd(x):
        return np.fft.fft(x,axis=1)/PROPOSAL_GRID
    def rhs(state):
        p = np.zeros((N+1,PROPOSAL_GRID),dtype=np.complex128)
        s = np.zeros_like(p)
        p[:,1:m.HEAD+1] = -1j*state[:,:m.HEAD]/np.sqrt(2)
        s[:,1:m.HEAD+1] = state[:,m.HEAD+1:]/np.sqrt(2)
        p[:,-m.HEAD:] = np.conj(p[:,m.HEAD:0:-1])
        s[:,-m.HEAD:] = np.conj(s[:,m.HEAD:0:-1])
        mean = state[:,m.HEAD:m.HEAD+1]
        s[:,0:1] = mean
        a,b,ap,bp = bwd(p),bwd(s),bwd(p*deriv),bwd(s*deriv)
        inner = bwd(prim*fwd(u*a+kv*b))
        return packed(fwd(force[:,0]+d*ap+a12*bp+l11*a+l12*b+n1*inner+m1*mean),
                      fwd(force[:,1]+d*bp+a21*ap+l21*a+l22*b+n2*inner+m2*mean))
    state = np.broadcast_to(right,(N+1,m.DIM)).copy()
    for _ in range(18):
        state = right+float(half)*(q@rhs(state))
    left = state[-1]
    x = pts[1:-1,None]
    linear = ((1-x)*left+(1+x)*right)/2
    cs = np.linalg.solve(np.vander(x[:,0],N-1,increasing=True),(state[1:-1]-linear)/(1-x*x))
    ans = np.ascontiguousarray(np.vstack((left,right,cs)),dtype="<f8")
    m.require(ans.shape==(N+1,m.DIM) and np.isfinite(ans).all(),"complete finite dyadic choice")
    return ans


class Trial:
    def __init__(self,bits,half):
        values = [[arb(float(v)) for v in row] for row in bits]
        left,right = values[:2]
        self.half = half
        self.center = [(l+r)/2 for l,r in zip(left,right)]
        self.slope = [(r-l)/2 for l,r in zip(left,right)]
        self.cs = list(zip(*values[2:]))
        # The Fourier A0 sum of both components costs at most two per real coordinate.
        def A(row):
            return 2*sum((abs(x) for x in row),arb(0))
        q = m.DISC
        U = sum((A(row)*q**i for i,row in enumerate(values[2:])),arb(0))
        Up = sum((i*A(row)*q**(i-1) for i,row in enumerate(values[2:]) if i),arb(0))
        self.bound = (A(self.center)+q*A(self.slope)+(1+q*q)*U).upper()
        self.bound_r = ((A(self.slope)+2*q*U+(1+q*q)*Up)/half).upper()

    def at(self,t):
        values,derivs = [],[]
        one = 1-t*t
        for a,b,cs in zip(self.center,self.slope,self.cs):
            p,dp = cs[-1],arb(0)
            for c in reversed(cs[:-1]):
                dp,p = dp*t+p,p*t+c
            values.append(a+t*b+one*p)
            derivs.append((b-2*t*p+one*dp)/self.half)
        return values,derivs


def cells(target,plan,root_hi,start):
    """Fixed geometric germs can straddle cubic or old-grid cuts, with all physical cuts retained."""
    chosen = [p for p in plan if p[2]<root_hi]
    ends = [p[3] for p in chosen]
    m.require(chosen[0][2]==0 and ends[-1]==root_hi and 0<=start<=root_hi,"true full original window")
    cuts = sorted({Fraction(0),root_hi,*[z for z in target.cuts if 0<z<root_hi],
                   Fraction(1,20),Fraction(9,50)})
    def groups(left,right,depth=0):
        if left>=start:
            return
        try:
            if right-left>Fraction(1,2048):
                raise ArithmeticError("deterministic grouping mesh")
            geom = m.Geometry(target,left,right)
        except (ValueError,ZeroDivisionError,ArithmeticError):
            m.require(depth<24,"actual analytic germ could not be certified")
            mid = (left+right)/2
            yield from groups(mid,right,depth+1)
            yield from groups(left,mid,depth+1)
            return
        end = min(start,right)
        i = bisect_right(ends,left)
        pieces = []
        while i<len(chosen) and chosen[i][2]<end:
            row,k,l,r = chosen[i]
            pieces.append((row,k,max(left,l),min(end,r)))
            i += 1
        m.require(pieces and pieces[0][2]==left and pieces[-1][3]==end and
                  all(a[3]==b[2] for a,b in zip(pieces,pieces[1:])),"whole geometric interval covered exactly once")
        for row,k,l,r in reversed(pieces):
            yield geom,row,k,l,r
    for l,r in reversed(list(zip(cuts,cuts[1:]))):
        yield from groups(l,r)


def run(target,base,offsets,plan,helper,private,checkpoint,start=None,initial=None):
    root_hi = helper.ROOT[1]
    start = root_hi if start is None else start
    right = np.zeros(m.DIM,dtype="<f8") if initial is None else initial.copy()
    nodes,quad = m.quadrature()
    weights = {False:[arb(1)]*(m.BAND+1),True:[(arb(1+16*k*k).log()/3).exp() for k in range(m.BAND+1)]}
    sums = {z:[arb(0),arb(0)] for z in ("strict","root","bracket")}
    chain = hashlib.sha256(b"ASQ27 fixed-geometry base Newton disjoint residual v1").digest()
    digest = hashlib.sha256()
    private = Path(private)
    private.mkdir(exist_ok=False)
    path = private/"new-full-continuous-dyadic-trials.f64"
    kprev = None
    old_ends = set(p[2] for p in plan if p[2]<root_hi)
    count = original = 0
    with path.open("xb") as stream:
        for geo,row,k,lo,hi in cells(target,plan,root_hi,start):
            m.require(hi==start and lo<hi and (hi<=helper.NEGATIVE_CUT or lo>=helper.NEGATIVE_CUT) and
                      (hi<=helper.ROOT[0] or lo>=helper.ROOT[0]),"contiguous backward true cells with both roots and cut split")
            if k!=kprev:
                raw = m.RawCubic(base,offsets,k)
                kprev = k
            half,mid = m.fm.rat((hi-lo)/2),m.fm.rat((hi+lo)/2)
            bracket = lo>=helper.ROOT[0]
            root = lo>=helper.NEGATIVE_CUT
            region = "bracket" if bracket else "root" if root else "strict"
            # Shared nodes are consumed once, with every original signed forcing term retained.
            cache = {} if bracket else {i:m.physical_node(raw,geo,mid+half*nodes[i])
                                         for i in range(0,m.GRID+1,m.GRID//N)}
            bits = select_trial(list(cache.values()),half,right,bracket)
            m.require(np.array_equal(bits[1],right),"no trial jump, including the independent mean")
            trial = Trial(bits,half)
            M = m.complex_cap(raw,geo,mid,half,trial.bound,trial.bound_r)
            e2,y2 = arb(0),arb(0)
            weights0 = weights[root]
            for i,(t,w) in enumerate(zip(nodes,quad)):
                force,operator = cache.pop(i) if i in cache else m.physical_node(raw,geo,mid+half*t)
                if bracket:
                    r2 = m.norm2(force,weights0)
                else:
                    y,dy = trial.at(t)
                    pair = m.reflected(y,m.HEAD,True)
                    dr = m.reflected(dy,m.HEAD,True)
                    applied = m.apply(operator,pair)
                    residual = tuple(f+a-v for f,a,v in zip(force,applied,dr))
                    r2 = m.norm2(residual,weights0)
                    y2 += w*sum((v**2 for v in y),arb(0))
                e2 += w*r2
            inv = m.fm.rat(Fraction(1,m.DISC))
            beyond = 2*weights0[-1]*M**2*inv**(m.GRID+1)/(1-inv)
            sums[region][0] += (2*half*(e2+beyond)).upper()
            sums[region][1] += (2*half*y2).upper()
            block = bits.tobytes()
            stream.write(block)
            stream.flush()
            digest.update(block)
            chain = hashlib.sha256(chain+hashlib.sha256(block).digest()).digest()
            right = bits[0].copy()
            start = lo
            count += 1
            original += int(lo in old_ends)
            checkpoint(count,original,row,k,lo,right,sums,path.stat().st_size,digest.hexdigest(),chain.hex())
    verify = hashlib.sha256()
    with path.open("rb") as stream:
        for part in iter(lambda:stream.read(1<<20),b""):
            verify.update(part)
    m.require(start==0 and path.stat().st_size==count*(N+1)*m.DIM*8 and verify.digest()==digest.digest(),
              "physical waist and complete newly selected trial readback")
    return right,sums,dict(bytes=path.stat().st_size,sha256=verify.hexdigest(),ordered_chain=chain.hex(),
                           subcells=count,original_cells=original)
