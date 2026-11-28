"""Nested material height space, genuine cap two-jets and explicit logarithmic deep extensions."""
import numpy as np
from scipy.interpolate import BSpline
from r738_macro_spline_space import CUT,OLD,RIM,distinct,radial_breaks
from r738_negative_tail_and_macro_source import SIGNS,RATIO,bounds_t,bump,THETA
from r748_paid_material_height_projection import QuinticHeight,original_fixed_reference
from r748_single_height_development import RadialGrid,smooth_join,fourier_height


def grid_edges(opt,stage,detail,seed_knots):
    depth=opt['tail_depths'][detail]
    knots=list(seed_knots)+list(radial_breaks(32,2,True))+[.105,.175,.085,.09,.145,.15,.205,.21,.083,.212]
    for s in SIGNS:
        for n in range(depth):
            L=np.ldexp(1/512,-n)
            knots.extend(RIM[s]-s*RATIO[s]*L*t for t in bounds_t(L))
        knots.append(RIM[s])
    knots.extend(np.linspace(OLD[-1],OLD[1],stage['spans']+1))
    edges=distinct(knots)
    return distinct(np.concatenate([np.linspace(l,h,opt['radial_splits'][detail]+1) for l,h in zip(edges,edges[1:])]))


def base_height(base,r,K):
    raw=base.paid(r)
    w=raw['omega'];p,dp=bump(r);wp=-base.M*p/r;wpp=-base.M*dp/r-wp/r
    s=np.sin(w);c=np.cos(w)
    out=np.zeros((3,len(r),K+1))
    out[:,:,0]=raw['center'][:,:,2].T
    out[:,:,1]=np.stack((-r*s,-s-r*c*wp,-2*c*wp+r*s*wp**2-r*c*wpp))
    return out


def log_extension(t,steps,rate,power=10):
    """Real linear extension; complex-step design perturbations remain intact."""
    a=steps[0];b=steps[1]/rate-power*a
    osc=np.pi/np.log(2.)
    c=(steps[2]/rate**2-(power*(power-1)-osc**2)*a-2*power*b)/2
    coeff=(a-b+c,b-2*c,c)
    result=np.zeros((3,len(t),len(a)),dtype=steps.dtype)
    active=t>0
    for k,ck in enumerate(coeff):
        h=power+k+1j*osc
        for d in range(3):
            fac=(1,h,h*(h-1))[d]
            shape=np.real(fac*np.exp((h-d)*np.log(t[active])))*rate**d
            result[d,active]+=shape[:,None]*ck
    return result,coeff


class HeightSpace:
    """All coefficients, including both edge triples, remain free on the actual donor interval."""
    def __init__(self,stage,seed,base,center):
        self.spans,self.K=stage['spans'],stage['K']
        self.center=np.asarray(center);self.seed=seed;self.base=base
        ends=np.linspace(OLD[-1],OLD[1],self.spans+1)
        self.knots=np.r_[[ends[0]]*5,ends,[ends[-1]]*5]
        n=len(self.knots)-6
        self.bs=BSpline(self.knots,np.eye(n),5,extrapolate=False)
        self.scales=np.ones(n)*.001
        # True free edge first/second jets are normalized to the corresponding physical cap width.
        # Value/first two coefficients collectively control each edge. Keep all of them.
        for side,s in enumerate(SIGNS):
            ix=slice(0,3) if side==0 else slice(-3,None)
            self.scales[ix]=abs(OLD[s]-RIM[s])**2*.04
        self.size=2+n*(self.K+1);self.cache={}
    def prolong(self,old,x):
        if self.spans%old.spans or self.K<old.K:raise ValueError('Non-nested parameter space.')
        coeff=x[2:].reshape((-1,old.K+1))*old.scales[:,None]
        b=BSpline(old.knots,coeff,5,extrapolate=False)
        for knot in self.knots[6:-6]:
            if knot not in b.t:b=b.insert_knot(knot)
        if not np.array_equal(b.t,self.knots):raise ArithmeticError('Exact knot insertion failed; dyadic grids must agree.')
        new=np.zeros((len(self.scales),self.K+1));new[:,:old.K+1]=b.c/self.scales[:,None]
        return np.r_[x[:2],new.ravel()]
    def prepare(self,grid):
        if grid in self.cache:return self.cache[grid]
        r=grid.r;rr=np.clip(r,OLD[-1],OLD[1])
        old,_=self.seed.coefficient_jets(rr);basis=np.stack([self.bs(rr,d)*self.scales for d in range(3)])
        seed=np.zeros((3,len(r),self.K+1));seed[:,:,:old.shape[-1]]=old
        bounds=[]
        for s in SIGNS:
            deep=(r<OLD[s]) if s==-1 else (r>OLD[s])
            at=0 if s==-1 else -1
            rate=1/(OLD[s]-RIM[s]);t=(r[deep]-RIM[s])*rate
            # Clipping supplies the actual original 0/1/2 cut jets to both continuations.
            seed[:,deep],sc=log_extension(t,seed[:,at],rate)
            basis[:,deep],bc=log_extension(t,basis[:,at],rate)
            bounds.append((np.stack(sc),np.stack(bc),rate))
        base=base_height(self.base,r,self.K)
        lift=np.stack([z[:,0,0] for z in smooth_join(r,.105,.175)])
        E,Ep=original_fixed_reference(self.base,r)
        self.cache[grid]=base+seed,basis,lift,E,Ep,bounds
        return self.cache[grid]
    def fields(self,grid,x):
        seed,basis,lift,E,Ep,edge=self.prepare(grid)
        c=np.asarray(x[2:]).reshape((-1,self.K+1))
        h=seed+basis@c
        # Cx,Cz are absolute physical pose coordinates. At the inner rim the true center-height is Cz.
        h[:,:,0]+=lift*(x[1]-self.base_inner_height)
        return h,E,Ep,edge
    def edge_coeff(self,grid,x):
        c=x[2:].reshape((-1,self.K+1))
        return [(a+b@c,rate) for a,b,rate in self.prepare(grid)[-1]]
    def jets(self,grid,phi,x):
        h,E,Ep,_=self.fields(grid,x)
        return fourier_height(phi,h,np.zeros_like(h)),E,Ep

