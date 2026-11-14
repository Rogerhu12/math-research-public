"""Algebraically identical source with a stable positive cap derivative.

The shared Jet and I classes are imported from the reviewed source module.
Only the evaluation of 1-S7(t) is factored; all source geometry is fixed.
The derivative polynomial is nonnegative and at most one on [0,1], so its
constant coefficient may be intersected with that range without changing
any higher normalized derivative coefficient.
"""
import numpy as np
from db6f_tail_interval_source import FrozenSource as OriginalSource, Jet, I, LOG2


class FrozenSource(OriginalSource):
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
        d=(1-tc)**4*(1+tc*(4+tc*(10+20*tc)))
        d.c[0]=I(np.maximum(0,d.c[0].lo),np.minimum(1,d.c[0].hi))
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
