"""Stream the R663 proof over the already populated native steps, retaining a portable anchor."""
from fractions import Fraction
import math

import r663_actual_dense_denominator_20261128 as base

iv=base.coef
I,rat,mag=iv.I,iv.rat,iv.mag


def frac(x):
    return Fraction.from_float(float(x))


def interval_pair(x):
    return [x.lo,x.hi]


class DenseStream:
    def __init__(self,obj,j,forced,ball,rate):
        self.obj,self.j,self.forced,self.ball=obj,j,forced,ball
        self.col=base.Column(obj,j,forced,math.inf,2**60,rate)
        self.path=[]
        extra=0
        last=float(obj.flat.alpha)
        for low,high,dense,L in obj.flat.segments:
            begin,end=float(dense.ts[0]),float(dense.ts[-1])
            if (begin,end)==(float(low),float(high)) and begin==float(obj.flat.alpha) and j in (18,20,22):
                extra+=1
                continue
            if begin!=last or end>=begin or (begin,end)!=(float(high),float(low)):
                raise ValueError('different original flat path')
            if not self.path and L!=0:
                raise ValueError('first flat segment has different amplitude')
            self.path.append(('flat',dense,float(L)))
            last=end
        if not self.path or abs(last-2.5)>1e-12:
            raise ValueError('incomplete normalization path')
        self.path.extend([('body',obj.forward.sol,0.),('core',obj.raw_core.sol,0.)])
        self.extra=extra
        self.ob=self.poly=None
        self.anchor=None
        self.err_by_chart={}
        self.bi=self.ni=0
        self.pending=[]
        self.budget_counts=dict(cells=0,accepted=0,native=0)
        self.flat_at_mouth=None

    def load(self):
        chart,dense,L=self.path[self.bi]
        if not hasattr(dense,'interpolants') or len(dense.ts)!=len(dense.interpolants)+1:
            raise LookupError('required native DOP853 coefficients absent')
        ob=dense.interpolants[self.ni]
        if ((float(ob.t_old),float(ob.t))!=(float(dense.ts[self.ni]),float(dense.ts[self.ni+1]))
                or ((ob.t>ob.t_old)!=(chart=='body'))):
            raise ValueError('disconnected native mesh')
        factors=(1,self.col.cfrac) if chart=='flat' else (1,1)
        indices=(0,1 if chart=='flat' or not self.forced else 2)
        self.col.chart=chart
        self.ob=ob
        self.poly=base.polynomial(ob,indices,factors)
        return chart,L

    def initial(self):
        chart,L=self.load()
        p=base.value(self.poly,I(0))
        b=self.ball
        if (chart!='flat' or L!=0 or float(self.ob.t_old).hex()!=b['paid_alpha_hex']
                or float(self.obj.flat.finite_inner_data['z_alpha_first']).hex()!=b['paid_z_hex']):
            raise ValueError('different paid finite Cauchy owner')
        z=I(*b['finite_z_at_exact_alpha'])
        db,dl=base.compare((I(1),z*self.col.c),p,I(0))
        q=I(120)*b['alpha_radius']
        self.col.b,self.col.lam=(I(db)+q).hi,(I(dl)+q).hi
        self.mark(0.)
        self.pending=[(0.,1.,0)]

    def mark(self,s):
        chart,dense,L=self.path[self.bi]
        x=frac(self.ob.t_old)+(frac(self.ob.t)-frac(self.ob.t_old))*frac(s)
        p=base.value(self.poly,I(s))
        self.anchor={'chart':chart,'x':str(x),'P':[interval_pair(v) for v in p],
                     'logscale':L,'angle':self.col.b,'lognorm':self.col.lam,
                     'block':self.bi,'step':self.ni,'s':s,
                     't0':float(self.ob.t_old).hex(),'t1':float(self.ob.t).hex()}

    def move(self):
        old=self.anchor
        p=tuple(I(*v) for v in old['P'])
        b,lam=old['angle'],old['lognorm']
        exact=rat(Fraction(old['x']))
        self.ni+=1
        if self.ni==len(self.path[self.bi][1].interpolants):
            self.bi+=1
            self.ni=0
        if self.bi==len(self.path):
            return False
        chart,L=self.load()
        q=base.value(self.poly,I(0))
        t=I(float(self.ob.t_old))
        if chart==old['chart']:
            if Fraction(old['x'])!=frac(self.ob.t_old):
                raise ValueError('gap in a source chart')
            b,lam=base.jump(p,q,b,lam,I(old['logscale'])-L)
        elif chart=='body' and old['chart']=='flat':
            self.flat_at_mouth=self.packet()
            self.flat_at_mouth['anchor']=old
            b,lam=base.bridge(exact,I(2.5),b,lam,lambda u: iv.flat(u,self.col.mu,self.col.c))
            u=I(2.5)
            r,e,_,_=iv.flat_parts(u,self.col.mu)
            w=iv.AMP*iv.exp(-u*(2-iv.sin(u)))
            k=w*r*u**2*e/((self.col.mu-1)*iv.ELL*self.col.c)
            bias=I(old['logscale'])-float(self.obj.flat.display_log)+self.col.mu*iv.log(r)
            b,lam=base.changed_chart(p,q,(I(0),k,-w,k),b,lam,bias)
            if base.width(t,iv.R0)>1e-12:
                raise ValueError('wrong radial mouth')
            b,lam=base.bridge(iv.R0,t,b,lam,self.col.generator)
        elif chart=='core' and old['chart']=='body':
            rx=iv.core_r(t)
            if base.width(exact,rx)>1e-12:
                raise ValueError('wrong core switch')
            b,lam=base.bridge(exact,rx,b,lam,lambda r: iv.body(r,self.col.mu,self.col.guard))
            w=iv.body_slope(rx,self.col.guard)[0]
            b,lam=base.changed_chart(p,q,(I(1),I(0),1/w,-1/w),b,lam)
        else:
            raise ValueError('unexpected order of original charts')
        self.col.b,self.col.lam=b,lam
        self.mark(0.)
        self.pending=[(0.,1.,0)]
        return True

    def restore(self,packet):
        # Prior source-bound FINAL proves a cone about the saved P at the exact physical coordinate.
        a=packet['anchor']
        self.bi,self.ni=a['block'],a['step']
        same=False
        if self.bi<len(self.path) and self.ni<len(self.path[self.bi][1].interpolants):
            chart,L=self.load()
            same=(chart==a['chart'] and float(self.ob.t_old).hex()==a['t0']
                  and float(self.ob.t).hex()==a['t1'])
        x=Fraction(a['x'])
        if same:
            s=a['s']
            if x!=frac(self.ob.t_old)+(frac(self.ob.t)-frac(self.ob.t_old))*frac(s):
                raise ValueError('wrong retained proof coordinate')
            self.pending=[tuple(v) for v in packet['pending']]
        else:
            # A proved cone at x is independent of an adaptive solver mesh. Locate it
            # using stored step times alone and bridge to the next exact dyadic abscissa.
            found=False
            for index,(chart,dense,L) in enumerate(self.path):
                if chart!=a['chart'] or not min(frac(dense.ts[0]),frac(dense.ts[-1]))<=x<=max(frac(dense.ts[0]),frac(dense.ts[-1])):
                    continue
                direction=1 if chart=='body' else -1
                lo,hi=0,len(dense.ts)-1
                while hi-lo>1:
                    mid=(lo+hi)//2
                    if direction*frac(dense.ts[mid])<=direction*x:
                        lo=mid
                    else:
                        hi=mid
                self.bi,self.ni=index,lo
                chart,L=self.load()
                f=(x-frac(self.ob.t_old))/(frac(self.ob.t)-frac(self.ob.t_old))
                s=math.ceil(f*(2**27))/(2**27)
                self.pending=[] if s==1 else [(s,1.,0)]
                found=True
                break
            if not found:
                raise ValueError('retained coordinate outside every native segment of its chart')
        self.col.b,self.col.lam=a['angle'],a['lognorm']
        p=base.value(self.poly,I(s))
        old=tuple(I(*v) for v in a['P'])
        if [interval_pair(v) for v in p]!=a['P'] or L!=a['logscale']:
            self.col.b,self.col.lam=base.jump(old,p,self.col.b,self.col.lam,I(a['logscale'])-L)
        newx=frac(self.ob.t_old)+(frac(self.ob.t)-frac(self.ob.t_old))*frac(s)
        if x!=newx:
            self.col.b,self.col.lam=base.bridge(rat(x),rat(newx),self.col.b,self.col.lam,self.col.generator)
        self.mark(s)
        self.err_by_chart=dict(packet['whole_chart_log_error_suprema'])
        self.budget_counts=dict(packet['cumulative_counts'])
        at=s
        for l,r,d in reversed(self.pending):
            if l!=at or not l<r<=1 or type(d) is not int or not 0<=d<=23:
                raise ValueError('incomplete remaining native step')
            at=r
        if at!=1:
            raise ValueError('missing remainder after the retained proof coordinate')

    def packet(self):
        return {'anchor':self.anchor,'pending':list(self.pending),
                'whole_chart_log_error_suprema':dict(self.err_by_chart),
                'cumulative_counts':dict(self.budget_counts)}

    def work(self,packet):
        if packet is None:
            self.initial()
        else:
            self.restore(packet)
        while True:
            if not self.pending:
                if not self.move():
                    break
            l,r,depth=self.pending[-1]
            t=I(float(self.ob.t_old))
            h=I(float(self.ob.t))-float(self.ob.t_old)
            b0=self.col.b
            self.budget_counts['cells']+=1
            try:
                self.col.tube(self.poly,t,h,l,r)
            except ArithmeticError:
                if depth==23:
                    raise
                mid=(l+r)/2
                self.pending[-1:]=[(mid,r,depth+1),(l,mid,depth+1)]
                yield
                continue
            self.pending.pop()
            self.budget_counts['accepted']+=1
            if r==1:
                self.budget_counts['native']+=1
            self.mark(r)
            # Absolute continuous 2-vector error on this cell versus its native polynomial,
            # in normalized flat coordinates (y,c*z) or the active physical body/core coordinates.
            p=base.value(self.poly,I(l,r))
            factor=iv.exp(I(self.col.lam))
            gain=(factor-1)+factor*max(b0,self.col.b)
            n2=p[0]**2+p[1]**2
            if gain.hi>0 and n2.hi>0:
                logerr=iv.log(I(n2.hi))/2+iv.log(I(gain.hi))
                chart=self.anchor['chart']
                if chart=='flat':
                    logerr=logerr+self.anchor['logscale']-float(self.obj.flat.display_log)
                self.err_by_chart[chart]=max(self.err_by_chart.get(chart,logerr.hi),logerr.hi)
            yield
        a=self.anchor
        if a['chart']!='core' or Fraction(a['x'])!=0:
            raise ValueError('proof did not reach the exact rim')
        p=tuple(I(*v) for v in a['P'])
        k=1 if self.forced else 0
        observed=float(self.obj.raw_core_C[0] if self.forced else self.obj.Acore)
        e=iv.exp(I(a['lognorm']))
        sigma=(iv.iv.sqrt_i(base.norm2(p))*((e-1)+e*a['angle'])+mag(p[k]-observed)).hi
        return {'proved_absolute_error_upper':sigma,'signed_observation_hex':observed.hex(),
                'meets_half_denominator_threshold':frac(sigma)<=abs(frac(observed))/2,
                'source_component':('forced_homogeneous_C' if self.forced else 'homogeneous_A'),
                'exact_rim_anchor':a,'whole_chart_log_error_suprema':self.err_by_chart,
                'cumulative_counts':dict(self.budget_counts),'unused_inward_extensions':self.extra}
