"""Complete R738 material space with two true tail ports and dependent central quintic jets."""
import numpy as np
from scipy.interpolate import BSpline
from r738_negative_tail_and_macro_source import A0,B0,THETA,FIRST,RATIO,MODES,SIGNS,bounds_t,mode_at,native_tail_spinor

RIM={-1:A0,1:B0}
CUT={s:RIM[s]-s*RATIO[s]*np.ldexp(1/512,-FIRST[s]) for s in SIGNS}
OLD={s:RIM[s]-s*RATIO[s]/512 for s in SIGNS}


def radial_breaks(spans,depth,all_negative):
    ends=np.linspace(CUT[-1],CUT[1],spans+1)
    values=list(ends)
    for sign in SIGNS:
        stop=0 if all_negative else min(0,FIRST[sign]+depth)
        for n in range(FIRST[sign],stop):
            L=np.ldexp(1/512,-n)
            for t in bounds_t(L):
                values.append(RIM[sign]-sign*RATIO[sign]*L*t)
    return distinct(values)


def distinct(values):
    out=[]
    for value in sorted(set(float(v) for v in values)):
        if out and value-out[-1]<=8*max(np.spacing(value),np.spacing(out[-1])):
            continue
        out.append(value)
    return np.asarray(out)


class Grid:
    def __init__(self,spans,order,split,depth):
        self.a,self.b,self.theta=A0,B0,THETA
        edges=radial_breaks(spans,depth,True)
        # Reference corners, the exact cutoff/cap traces, and high/low transition surfaces
        # are always actual rows. Near seams no second copy separated by a roundoff ulp is made.
        edges=distinct(np.r_[edges,.085,.09,.145,.15,.205,.21,A0+.008,B0-.008])
        if split>1:
            edges=distinct(np.concatenate([np.linspace(p,q,split+1) for p,q in zip(edges,edges[1:])]))
        t,w=np.polynomial.legendre.leggauss(order);inter=[];weights=[]
        for a,b in zip(edges,edges[1:]):
            if not b>a:raise ArithmeticError('Nonincreasing physical tissue cuts.')
            rr=(a+b)/2+(b-a)*t/2
            if rr[0]<=a or rr[-1]>=b:raise ArithmeticError('Radial quadrature collides with an actual material knot.')
            inter.extend([a,*rr]);weights.extend([0.,*((b-a)*w/2)])
        inter.append(edges[-1]);weights.append(0.)
        self.r=np.r_[A0,inter,B0];self.w=np.r_[OLD[-1]-A0,weights,B0-OLD[1]]
        self.guard=np.r_[(self.r[1]-self.r[0])/2,(self.r[2:]-self.r[:-2])/2,(self.r[-1]-self.r[-2])/2]
        self.deep_radial_length_error_upper=4.e-17


class PhysicalFields:
    def __init__(self,base,cells,count,ray=1):
        self.base,self.cells,self.count,self.ray=base,cells,count,ray
        self.rows={};self.modes={}
    def prepare(self,r):
        full=np.array(sorted(set(float(z) for z in r).difference(self.rows)))
        if not len(full):return
        data=self.base.paid(full)
        for i,key in enumerate(full):
            self.rows[key]=(data['zb'][i],data['center'][i],data['reference_E'][i])
            for sign in SIGNS:
                if not (key<=CUT[sign] if sign==-1 else key>=CUT[sign]):continue
                if key==RIM[sign]:
                    self.modes[sign,key]={j:np.zeros((2,3,3)) for j in MODES}
                else:
                    self.modes[sign,key]={j:mode_at(self.cells[sign,j],j,sign,key) for j in MODES}
                self.count['native_physical_new_tail_radius_reads']+=1
    def raw(self,r):
        self.prepare(r)
        return tuple(np.stack([self.rows[float(v)][j] for v in r]) for j in range(3))


class Layout:
    def __init__(self,spans,K,depth,fields,amplitude_scale):
        self.spans,self.K,self.depth,self.fields=spans,K,depth,fields
        self.space=self;self.nd=self.nf=2*K+1
        self.central=np.linspace(CUT[-1],CUT[1],spans+1)
        self.core=self.make_basis(self.central)
        self.breaks=radial_breaks(spans,depth,False)
        old_joins=[RIM[s]-s*RATIO[s]*np.ldexp(1/512,-n) for s in SIGNS for n in range(FIRST[s],1)]
        interior=np.concatenate([np.repeat(v,3 if v in old_joins else 1) for v in self.breaks[1:-1]])
        knots=np.r_[[self.breaks[0]]*6,interior,[self.breaks[-1]]*6]
        self.free=BSpline(knots,np.eye(len(knots)-6),5,extrapolate=False)
        nf=self.free.c.shape[0]-6
        def column_scale(i):
            lengths=np.diff(knots[i:i+7]);positive=lengths[lengths>0]
            return min(1.,positive.min()/.007)**2
        self.coefficient_scales=np.array([column_scale(i) for i in range(3,3+nf)])
        self.shapes=((nf,self.nf),(nf,self.nf),(nf+1,2),(2,2))
        self.offset=np.r_[0,np.cumsum([int(np.prod(a)) for a in self.shapes])]
        self.size=int(self.offset[-1]);self.amplitude_scale=np.asarray(amplitude_scale)
    @staticmethod
    def make_basis(b):
        t=np.r_[[b[0]]*5,b,[b[-1]]*5]
        return BSpline(t,np.eye(len(t)-6),5,extrapolate=False)
    def split(self,x):
        return tuple(np.asarray(x[a:b]).reshape(sh) for a,b,sh in zip(self.offset[:-1],self.offset[1:],self.shapes))
    def pack(self,cs):return np.concatenate([z.ravel() for z in cs])
    def free_basis(self,r,i):
        inside=(r>=self.breaks[0])&(r<=self.breaks[-1])
        m=np.zeros((len(r),self.free.c.shape[0]))
        m[inside]=self.free(r[inside],i)
        shape=m[:,3:-3]*self.coefficient_scales
        translation=m[:,:3].sum(axis=1)
        if i==0:translation[r<self.breaks[0]]=1.
        return shape,np.column_stack((translation,shape))
    def tail(self,sign,r,amps):
        vals={j:np.stack([self.fields.modes[sign,float(z)][j][:,:,self.fields.ray] for z in r],axis=-1) for j in MODES}
        return native_tail_spinor(vals,amps,sign,self.K)
    def actual_jets(self,r,cs):
        r=np.asarray(r);za,zb,cc,q=cs;amps=q*self.amplitude_scale
        base,ctr,_=self.fields.raw(r)
        self.fields.prepare([CUT[-1],CUT[1]])
        out=[[],[],[]];center=(r>CUT[-1])&(r<CUT[1]);dtype=np.result_type(za,zb,cc,q)
        for i in range(3):
            shapes,points=self.free_basis(r,i)
            aa=shapes@za;bb=shapes@zb;bb[:,0]+=base[:,i]
            c=ctr[:,i].astype(dtype,copy=True);c[:,[0,2]]+=points@cc
            out[0].append(aa);out[1].append(bb);out[2].append(c)
        for side,sign in enumerate(SIGNS):
            on=(r<=CUT[sign]) if sign==-1 else (r>=CUT[sign])
            at=np.array([CUT[sign]])
            three=self.tail(sign,at,amps[side]);ref=self.fields.rows[CUT[sign]][0]
            if np.any(on):
                used=self.tail(sign,r[on],amps[side])
                for i in range(3):
                    out[0][i][on]+=used[0][i]
                    out[1][i][on]+=used[1][i]
                    out[1][i][on,0]-=base[on,i]
            if not np.any(center):continue
            order=[0,1,2] if sign==-1 else [-1,-2,-3]
            a=self.central if sign==-1 else -self.central[::-1]
            h1,h2=np.diff(a)[:2]
            for b in (0,1):
                v,dr,dd=[z[0].copy() for z in three[b]]
                if b:
                    v[0]-=ref[0];dr[0]-=ref[1];dd[0]-=ref[2]
                dr=-sign*dr
                c0=v;c1=v+h1*dr/5;c2=c1+(h1+h2)*(dr+h1*dd/4)/5
                coef=np.stack((c0,c1,c2))
                for i in range(3):
                    out[b][i][center]+=self.core(r[center],i)[:,order]@coef
        return tuple(tuple(v) for v in out)
    def masks(self,r):
        base=[self.free_basis(r,i) for i in range(3)]
        masks=[]
        for k,(nr,ncol) in enumerate(self.shapes[:3]):
            use=int(k==2)
            live=np.logical_or.reduce([q[use]!=0 for q in base])
            for i in range(nr):masks.extend([np.flatnonzero(live[:,i])]*ncol)
        for sign in SIGNS:
            col=np.flatnonzero(r<self.central[3] if sign==-1 else r>self.central[-4])
            masks.extend([col]*2)
        return masks
    def prolong(self,old,x):
        if self.K<old.K or self.spans%old.spans or self.depth<old.depth:
            raise ValueError('R738 nested spaces required.')
        from scipy.linalg import qr,solve_triangular,svdvals
        source=old.split(x)
        parts=[np.zeros(sh) for sh in self.shapes]
        parts[3][:]=source[3];parts[2][0]=source[2][0]
        t=self.free.t;p=5
        greville=np.array([np.mean(t[i+1:i+p+1]) for i in range(len(t)-p-1)])
        r=greville[3:-3]
        a=old.actual_jets(r,source)
        b=self.actual_jets(r,parts)
        mat=self.free_basis(r,0)[0]
        Q,R=qr(mat,mode='economic',check_finite=False);sv=svdvals(R)
        if sv[-1]<=np.finfo(float).eps*len(sv)*sv[0]:raise ArithmeticError('Full Greville transport is rank deficient.')
        for j in range(3):
            if j<2:
                target=np.zeros_like(b[j][0]);target[:,:a[j][0].shape[1]]=a[j][0]
                parts[j][:]=solve_triangular(R,Q.T@(target-b[j][0]))
            else:
                parts[j][1:]=solve_triangular(R,Q.T@(a[j][0][:,[0,2]]-b[j][0][:,[0,2]]))
        self.last_greville=dict(rows=len(sv),all_singular_values=sv.tolist(),exact_nested_space=True,
                      former_clamps_have_C2_multiplicity_three=True)
        return self.pack(parts)
