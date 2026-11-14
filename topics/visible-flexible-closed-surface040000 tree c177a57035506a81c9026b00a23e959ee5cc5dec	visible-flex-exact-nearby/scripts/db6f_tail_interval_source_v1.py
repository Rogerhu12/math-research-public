"""Taylor interval algebra and the frozen finite weighted-tail source.

Coefficients of a Jet are normalized derivatives f^(k)/k!. Evaluating the
same algebra at an interval in the constant coefficient encloses these
derivatives at every point of that interval. Branch-crossing flags prohibit
use of a high-order Taylor remainder across nonanalytic cap/absolute-value
interfaces. The caller can subdivide or use a direct range integral there.
"""
import math
import numpy as np
from db6f_tail_interval_elementary import I, exp as iexp, log as ilog, LOG2


def choose(mask, yes, no):
    return I(np.where(mask, yes.lo, no.lo), np.where(mask, yes.hi, no.hi))


def hull(a, b):
    return I(np.minimum(a.lo, b.lo), np.maximum(a.hi, b.hi))


class Jet:
    def __init__(self, coefficients):
        self.c = coefficients
        self.order = len(coefficients)-1

    @classmethod
    def constant(cls, value, order):
        value = I.get(value)
        return cls([value]+[I(np.zeros(value.lo.shape)) for _ in range(order)])

    @classmethod
    def variable(cls, value, order):
        ans = cls.constant(value, order)
        if order:
            ans.c[1] = I(np.ones(ans.c[0].lo.shape))
        return ans

    def get(self, b):
        if isinstance(b, Jet):
            if b.order != self.order:
                raise ValueError('Taylor orders differ')
            return b
        return Jet.constant(b, self.order)

    def __add__(self, b):
        b = self.get(b)
        return Jet([a+z for a,z in zip(self.c,b.c)])

    __radd__ = __add__

    def __neg__(self):
        return Jet([-a for a in self.c])

    def __sub__(self, b):
        return self + (-self.get(b))

    def __rsub__(self, b):
        return self.get(b)+(-self)

    def __mul__(self, b):
        b = self.get(b)
        out = []
        for n in range(self.order+1):
            value = I(0)
            for k in range(n+1):
                value = value+self.c[k]*b.c[n-k]
            out.append(value)
        return Jet(out)

    __rmul__ = __mul__

    def reciprocal(self):
        out = [I(1)/self.c[0]]
        for n in range(1,self.order+1):
            value = I(0)
            for k in range(1,n+1):
                value = value+self.c[k]*out[n-k]
            out.append(-out[0]*value)
        return Jet(out)

    def __truediv__(self, b):
        return self*self.get(b).reciprocal()

    def __rtruediv__(self, b):
        return self.get(b)*self.reciprocal()

    def __pow__(self, n):
        if not isinstance(n,int) or n < 0:
            raise ValueError('nonnegative integral jet power required')
        if n == 0:
            return self.get(1)
        out, base = self.get(1), self
        while n:
            if n&1:out=out*base
            n//=2
            if n:base=base*base
        return out

    def exp(self):
        out = [iexp(self.c[0])]
        for n in range(1,self.order+1):
            value = I(0)
            for k in range(1,n+1):
                value=value+k*self.c[k]*out[n-k]
            out.append(value/n)
        return Jet(out)

    def sqrt(self):
        out=[self.c[0].sqrt()]
        for n in range(1,self.order+1):
            value=self.c[n]
            for k in range(1,n):value=value-out[k]*out[n-k]
            out.append(value/(2*out[0]))
        return Jet(out)

    @staticmethod
    def select(mask,yes,no):
        return Jet([choose(mask,a,b) for a,b in zip(yes.c,no.c)])

    @staticmethod
    def hull(a,b):
        return Jet([hull(x,y) for x,y in zip(a.c,b.c)])


class FrozenSource:
    def __init__(self, parameters, frozen):
        self.p = p = parameters
        self.frozen = frozen
        for key,value in frozen['calibrationParameters'].items():
            if p.get(key)!=value:
                raise ValueError('frozen source parameter changed: '+key)
        if len(frozen['constants'])!=160 or p['protectCell']!=160:
            raise ValueError('requires exactly the frozen finite 160 cells')
        if p['orientation']!=1 or p['capMode']!='cut-preserving' or p.get('flatOuterThroughCell',-1)>=0 or p.get('rejoinR20At') is not None:
            raise ValueError('unsupported profile convention')
        self.delta0=I(p['delta0']);self.c0=I(p['etaRatioAtN0']);self.eta0=self.delta0*self.c0
        self.root12=I(12).sqrt();self.q=I(1)/(2*I(2).sqrt())
        self.a=I(p['a']);self.cuff=I(p['rCuff']);self.cut=I(p['rCut'])
        self.logdelta=ilog(self.delta0);self.logwcut=ilog(I(p['wCut']))
        self.total=6*self.delta0+6*self.eta0/(1-self.q)
        self.oldcut=self.cuff*iexp(self.total/self.root12)
        self.cells={}

    def cell(self,n):
        if n in self.cells:return self.cells[n]
        if not 0<=n<160:raise ValueError('finite source cell out of range')
        p=self.p
        d=self.delta0/(2**n);eta=self.eta0
        for _ in range(n):eta=eta*self.q
        after=3*d+6*eta*self.q/(1-self.q)
        ld=self.logdelta-n*LOG2
        cal=pcal=self.frozen['constants'][n]['value']
        if float.fromhex(self.frozen['constants'][n]['hex'])!=cal:
            raise ValueError('calibration binary identity mismatch')
        R=p['prefixRByCell'][n] if n<=p['prefixEnd'] else p['R']
        beta=p['valleyControls'][n] if n<len(p['valleyControls']) else 0
        platform=[ld,ilog(I(R)),2*ld-ilog(I(cal))+beta,I(0),ld+self.a*LOG2]
        desc=[(0,0,eta),(0,1,eta),(1,1,d),(1,2,eta),(2,2,d),(2,3,eta),(3,3,d),(3,4,eta),(4,4,eta)]
        pulse=p.get('pulseCaps',[]);valley=p.get('valleyCaps',[])
        pulse=pulse[n] if n<len(pulse) else [p['slopeCap'],p['slopeCap']]
        valley=valley[n] if n<len(valley) else p['slopeCap']
        levels=[p['slopeCap'],pulse[0],valley,pulse[1],p['slopeCap']]
        weights=p.get('warpWeightLevels',[]);weights=weights[n] if n<len(weights) else [1]*5
        off=I(0);segments=[]
        for j,(l,h,length) in enumerate(desc):
            segments.append({'j':j,'length':length,'offset':off,'lo':platform[l],'hi':platform[h],
                             'transition':l!=h})
            off=off+length
        out={'n':n,'delta':d,'eta':eta,'after':after,'segments':segments,
             'capLevels':levels,'logCaps':[ilog(I(v)) for v in levels],
             'weights':weights,'logWeights':[ilog(I(v)) for v in weights]}
        self.cells[n]=out
        return out

    def evaluate(self,n,j,x):
        """Return A, B jets and analyticity flags for this source profile."""
        c=self.cell(n);seg=c['segments'][j];p=self.p;order=x.order
        C=lambda z:Jet.constant(z,order)
        S=x*x*x*(10+x*(-15+6*x));Sd=30*x*x*(1-x)*(1-x)
        # Tight range for the constant coefficient. Higher coefficients
        # remain the derivative enclosures from polynomial Jet algebra.
        xl,xh=I(x.c[0].lo),I(x.c[0].hi)
        sl=xl*xl*xl*(10+xl*(-15+6*xl));sh=xh*xh*xh*(10+xh*(-15+6*xh))
        S.c[0]=I(np.maximum(0,sl.lo),np.minimum(1,sh.hi))
        shape=C(seg['lo'])+(S*(seg['hi']-seg['lo']) if seg['transition'] else 0)
        shape_d=Sd*(seg['hi']-seg['lo']) if seg['transition'] else C(0)
        distance=C(c['after']+seg['offset'])+x*seg['length']
        raw=(C(self.logwcut-self.a*LOG2-(self.a-1)*n*LOG2-self.logdelta)
             +(C(self.total)-distance)*(I(7)/self.root12)+shape)
        raw_d=C(-7*seg['length']/self.root12)+shape_d
        if j%2==0:
            k=j//2;lc=C(c['logCaps'][k]);lc_d=C(0);weight=C(c['weights'][k]);fixedcap=c['capLevels'][k]
        else:
            k=(j-1)//2;lc=C(c['logCaps'][k])+S*(c['logCaps'][k+1]-c['logCaps'][k])
            lc_d=Sd*(c['logCaps'][k+1]-c['logCaps'][k]);weight=(C(c['logWeights'][k])+S*(c['logWeights'][k+1]-c['logWeights'][k])).exp()
            fixedcap=c['capLevels'][k] if c['capLevels'][k]==c['capLevels'][k+1] else None
        L=p['capTransition'];t=(raw-lc+L)/(2*L)
        low=t.c[0].hi<=0;high=t.c[0].lo>=1;inside=(t.c[0].lo>=0)&(t.c[0].hi<=1)
        analytic=low|high|inside
        # This polynomial is only used as an analytic branch when the whole
        # argument interval lies in [0,1]. Uncertain boxes get a range hull.
        tc=Jet(list(t.c));tc.c[0]=I(np.clip(t.c[0].lo,0,1),np.clip(t.c[0].hi,0,1))
        # On a crossing box only t in [0,1] belongs to the middle branch.
        # Restricting its value interval while retaining derivative bounds
        # encloses that subset; exterior branches are added below.
        J=tc**5*(7+tc*(-14+tc*(10-2.5*tc)))
        middle=lc-L+2*L*(tc-J)
        d=1-tc**4*(35+tc*(-84+tc*(70-20*tc)))
        middle_d=d*raw_d+(1-d)*lc_d
        logw=Jet.select(low,raw,Jet.select(high,lc,middle))
        logwd=Jet.select(low,raw_d,Jet.select(high,lc_d,middle_d))
        bad=~analytic
        uncertain=Jet.select(t.c[0].lo<0,Jet.hull(raw,middle),middle)
        uncertain_d=Jet.select(t.c[0].lo<0,Jet.hull(raw_d,middle_d),middle_d)
        uncertain=Jet.select(t.c[0].hi>1,Jet.hull(uncertain,lc),uncertain)
        uncertain_d=Jet.select(t.c[0].hi>1,Jet.hull(uncertain_d,lc_d),uncertain_d)
        logw=Jet.select(bad,uncertain,logw)
        logwd=Jet.select(bad,uncertain_d,logwd)
        const_w=high if fixedcap is not None else np.zeros(np.broadcast_shapes(x.c[0].lo.shape,analytic.shape),dtype=bool)
        if n==0 and j==7:
            logwd=Sd*(raw-logw)+S*raw_d+(1-S)*logwd
            logw=S*raw+(1-S)*logw
            const_w=np.zeros_like(analytic,dtype=bool)
        elif n==0 and j==8:
            logw,logwd=raw,raw_d;analytic=np.ones_like(analytic,dtype=bool);const_w=np.zeros_like(analytic,dtype=bool)
        w=logw.exp();wd=w*logwd
        if fixedcap is not None:
            w=Jet.select(const_w,C(fixedcap),w);wd=Jet.select(const_w,C(0),wd)
        E=1+w*w;rs=(distance/self.root12).exp()*self.cuff;rx=rs*(seg['length']/self.root12)
        chi=1-S if n==0 and j==8 else S if n==159 and j==0 else C(1)
        j0=1+S*(self.cut/self.oldcut-1) if n==0 and j==8 else C(1)
        signpos=wd.c[0].lo>=0;signneg=wd.c[0].hi<=0
        abswd=Jet.select(signpos,wd,Jet.select(signneg,-wd,Jet.hull(wd,-wd)))
        abswd.c[0]=wd.c[0].abs()
        A=rx*j0*(1-chi)+chi*abswd/(p['curvatureBound']*E*E.sqrt())
        A=Jet.select(const_w,rx*j0*(1-chi),A)
        B=chi*rx/E*weight
        validA=analytic&(signpos|signneg|const_w)
        return {'A':A,'B':B,'validA':validA,'validB':analytic,'w':w,'wd':wd}
