#!/usr/bin/env python3
"""Whole original M12 prefix source and exact-root target analytic pieces.

This supplies the already-defined up/down ramps, exact-root bridge, original
chart cutoff, and original common-cut correction to the correlated Gram
consumer. It changes no source coefficient or target parameter.
"""
from __future__ import annotations
import hashlib,importlib.util,json,math,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np

def load(name,path):
    if name in sys.modules:return sys.modules[name]
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
base=load('m12_prefix_total_local_engine',Path(__file__).with_name('m12-prefix-total-gram-local.py'))
kern=base.kern;I,Jet,LD=kern.I,kern.Jet,kern.LD;arrq=base.arrq;fq=base.fq
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def polyadd(a,b):
    n=max(len(a),len(b));return [(a[j] if j<len(a) else I(0))+(b[j] if j<len(b) else I(0)) for j in range(n)]
def polymul(a,b):
    c=[I(0) for _ in range(len(a)+len(b)-1)]
    for j,v in enumerate(a):
        for k,w in enumerate(b):c[j+k]=c[j+k]+v*w
    return c
def polypow(a,n):
    out=[I(1)]
    for _ in range(n):out=polymul(out,a)
    return out

class BridgeTarget:
    """True exact-root target f, with accurate values and exact derivative jets."""
    def __init__(self,bridge,offset,sine_degree=31):
        self.L=I.bounds(F(bridge['exact_L']['lo']),F(bridge['exact_L']['hi']))
        self.pt=I.bounds(F(bridge['exact_pt']['lo']),F(bridge['exact_pt']['hi']))
        self.ps=I.bounds(F(bridge['exact_ps']['lo']),F(bridge['exact_ps']['hi']))
        self.offset=offset;self.A=3*self.pt-self.L*self.ps;self.B=-2*self.pt+self.L*self.ps
        self.phi=[I(0),I(0),self.A,self.B]
        if sine_degree<15 or sine_degree%2!=1:raise ValueError('Odd sine truncation >=15 required')
        # Cubic Bernstein controls on a fixed slightly extended interval.
        tl,tr=F(-1,100),F(101,100);width=tr-tl
        power=[sum((math.comb(k,j)*self.phi[k]*tl**(k-j)*width**j for k in range(j,4)),I(0)) for j in range(4)]
        bern=[sum((power[j]*F(math.comb(k,j),math.comb(3,j)) for j in range(k+1)),I(0)) for k in range(4)]
        M=max(float(v.abs_upper()) for v in bern)
        # A simple exact ceiling contains every certified Bernstein control.
        bound=F(math.ceil(M*1000)+1,1000)
        if any(kern.exact(v.abs_upper())>bound for v in bern):raise ArithmeticError('Exact proposed bridge phase ceiling failed')
        if bound>=kern.exact(kern.PI.lo):raise ValueError('Bridge phase monotonicity requires a bound below pi')
        # phi=t^2(A+B t)>0 on the extended domain, except t=0.
        if (self.A+self.B*I.bounds(tl,tr)).lo<=0:raise ValueError('Bridge sine sign unresolved')
        self.domain=(tl,tr)
        self.error=self.L*F(101,100)*I(bound)**(sine_degree+1)/math.factorial(sine_degree+1)
        square=polymul(self.phi,self.phi);term=self.phi;sp=[I(0)]
        for degree in range(1,sine_degree+1,2):
            factor=F((-1)**((degree-1)//2),math.factorial(degree))
            sp=polyadd(sp,[v*factor for v in term]);term=polymul(term,square)
        self.primitive=[I(0)]+[v/(j+1) for j,v in enumerate(sp)]
        self.audit={'sine_degree':sine_degree,'phase_bound_exact':str(bound),
            'extended_normalized_domain':[str(tl),str(tr)],'primitive_uniform_error_upper_exact':str(kern.exact(self.error.hi)),
            'actual_derivative_is_minus_sin_phi':True,'original_exact_root_parameters_retained':True}
    def value(self,q):
        q=kern.base(q);t=(q-self.offset)/self.L
        if np.any(t.lo<I(self.domain[0]).lo) or np.any(t.hi>I(self.domain[1]).hi):raise ValueError('Outside certified bridge analytic extension')
        def direct(x):return (1-self.L*kern.poly(self.primitive,(x-self.offset)/self.L)).widen(self.error)
        if np.any(q.hi-q.lo>LD('1e-10')):
            # The certified cubic has phi in [0,pi) on this extension, so
            # the exact primitive f is nonincreasing for each fixed root.
            low=direct(I(q.hi));high=direct(I(q.lo));return I(low.lo,high.hi)
        return direct(q)
    def __call__(self,q):
        value=self.value(q)
        if not isinstance(q,Jet):return value
        t=(q-self.offset)/self.L;sn=kern.sincos(self.A*t*t+self.B*t*t*t)[0]
        c=[value]
        for n in range(1,q.order+1):c.append(-sum((j*q.c[j]*sn.c[n-j] for j in range(1,n+1)),I(0))/n)
        return Jet(c)

class RampTarget:
    """The exact prescribed ramp in its own small analytic-piece coordinate."""
    def __init__(self,left,right,coefficients):self.left=left;self.width=right-left;self.coefficients=coefficients
    def __call__(self,q):return kern.poly(self.coefficients,(q-self.left)/self.width)

class FullSource:
    def __init__(self,raw,meta,bridge,supplier,old,query_report,query_cache,solver_result):
        self.raw,self.meta,self.bridge,self.supplier,self.old=raw,meta,bridge,supplier,old
        self.mesh=list(map(fq,raw['mesh']));self.end=self.mesh[-1];cfg=meta['frozen_profile']
        self.delta,self.vu,self.vd,self.eps,self.eta=[fq(cfg[k]) for k in ('delta','vu','vd','ramp','ramp_eta')]
        self.Tu=self.delta/(self.vu*(1-self.eps));self.Td=self.delta/(self.vd*(1-self.eps));self.offset=self.Tu+self.Td
        self.Slo=self.offset+F(bridge['exact_L']['lo']);self.Shi=self.offset+F(bridge['exact_L']['hi']);self.S=I.bounds(self.Slo,self.Shi)
        self.lam=self.end/self.S;self.total=self.S+(fq(.6)-fq(.15));self.h=self.Tu*self.eps
        self.lamlo=self.end/self.Shi;self.lamhi=self.end/self.Slo
        self.Klo=self.end*(self.Shi+fq(.6)-fq(.15))/self.Shi;self.Khi=self.end*(self.Slo+fq(.6)-fq(.15))/self.Slo
        cut,chart=supplier.exact_clamped_spline(meta['chart']);self.cut,self.chart=cut,chart;self.warp=8*fq(meta['warp_reference_q'])
        self.chart_pieces=[];cuts=sorted(set(cut+[F(3,4)]))
        for l,r in zip(cuts[:-1],cuts[1:]):
            mid=(l+r)/2;j=min(__import__('bisect').bisect_right(cut,mid)-1,len(chart)-1);coeff=chart[j]
            cutoff=mid>=F(3,4)
            if cutoff:coeff=supplier.mul(coeff,supplier.compose([F(1),0,0,-10,15,-6],[4*cut[j]-3,F(4)]))
            self.chart_pieces.append({'left':l*self.end,'right':r*self.end,'source_index':j,'origin':cut[j],
                                      'coefficients':[self.warp*v for v in coeff],'cutoff_active':cutoff})
        target=supplier.Target.__new__(supplier.Target);target.eps=self.eps;target.eta=self.eta;target.sign=1;target.delta=self.delta
        e,h=self.eps,self.eta;us=[F(0),e*h,e*(1-h),e,1-e,1-e+e*h,1-e*h,F(1)];self.target_pieces=[]
        for phase,T,start in ((0,self.Tu,F(0)),(1,self.Td,self.Tu)):
            for j,(l,r) in enumerate(zip(us,us[1:])):
                ql,qr=start+T*l,start+T*r
                self.target_pieces.append({'native_left':self.lamlo*ql,'native_right':self.lamhi*qr,
                    'physical_left':ql,'physical_right':qr,'kind':'up-ramp' if phase==0 else 'down-ramp',
                    'piece':j,'evaluator':RampTarget(ql,qr,target.a_prefix_poly(ql,qr,(phase,T,start,j)))})
        self.bridge_target=BridgeTarget(bridge,self.offset)
        self.target_pieces.append({'native_left':self.lamlo*self.offset,'native_right':self.end,
             'physical_left':self.offset,'physical_right':None,'kind':'exact-root-bridge','piece':0,'evaluator':self.bridge_target})
        self.native_cache={};self.setup_common_cut(query_report,query_cache,solver_result)
    def setup_common_cut(self,report_path,cache_path,result):
        report=json.loads(Path(report_path).read_text())
        if report.get('source_regularization') or not report['original_exact_source_unchanged'] or not report['original_g_unchanged']:
            raise ValueError('Common-cut source must be the original Q-free exact stream')
        if sha(cache_path)!=report['endpoint_cache_sha256'] or sha(report_path)!=result['query_report_sha256'] or sha(cache_path)!=result['query_cache_sha256']:
            raise ValueError('Actual saved source-query binding differs')
        if report['manifest_sha256']!=self.meta['tail_manifest_sha256']:raise ValueError('Original endpoint manifest differs')
        with np.load(cache_path,allow_pickle=False) as z:
            exact=[F(int(a),int(b)) for a,b in zip(z['endpoint_numerator'],z['endpoint_denominator'])]
            rows=[exact,[fq(x) for x in z['first']],[fq(x) for x in z['second']]];pm=list(map(int,z['planar_modes']));hm=list(map(int,z['height_modes']))
        M=int(self.meta['modes']);oldM=(self.raw['jets'].shape[-1]-2)//3;P=len(pm);lookup={k:j for j,k in enumerate(pm)}
        if M<max(oldM,max(abs((k-1)//3) for k in pm),max(k//3 for k in hm)):raise ValueError('Common-cut Fourier support incomplete')
        T=[[F(0)]*(3*M+2) for _ in range(3)];Y=[[F(0)]*(3*M+2) for _ in range(3)]
        for d,row in enumerate(rows):
            def get(k):return row[lookup[k]] if k in lookup else F(0)
            T[d][0]=get(1)
            for j in range(1,M+1):T[d][j]=get(1+3*j)+get(1-3*j);T[d][M+j]=get(1+3*j)-get(1-3*j)
            for j,k in enumerate(hm):T[d][-1 if k==0 else 2*M+k//3]=-row[P+j]
            y=list(map(fq,self.raw['jets'][d,-1]));Y[d][0]=y[0];Y[d][-1]=y[-1]
            for axis in range(3):Y[d][axis*M+1:axis*M+oldM+1]=y[axis*oldM+1:(axis+1)*oldM+1]
        cut=F(self.bridge['physical_cut_radius_exact']);w=F(1,2);wr=-7*w/cut;E=1+w*w
        T[0][0]+=cut;T[1][0]+=1;T[0][-1]=Y[0][-1];T[1][-1]-=w;T[2][-1]-=wr
        T,Y=arrq(T),arrq(Y);k=-I(1)/I(E).sqrt();k2=-w*wr/(E*E)
        target=[T[0],T[1]*(k/self.lam),(T[2]/E+T[1]*k2)/(self.lam*self.lam)]
        delta=[target[j]-Y[j] for j in range(3)];delta[0].lo[-1]=delta[0].hi[-1]=0
        self.common_start=int(self.meta['correction_start_index']);self.common_left=self.mesh[self.common_start];self.common_width=self.end-self.common_left;h=self.common_width
        self.common_poly=[10*delta[0]-4*h*delta[1]+h*h*delta[2]/2,
                         -15*delta[0]+7*h*delta[1]-h*h*delta[2],
                         6*delta[0]-3*h*delta[1]+h*h*delta[2]/2]
        self.M=M;self.oldM=oldM
        self.common_audit={'query_report_sha256':sha(report_path),'query_cache_sha256':sha(cache_path),
            'exact_endpoint_numerator_denominator_consumed':True,'first_second_are_exact_original_binary64':True,
            'cut_native_cell':self.common_start,'cut_native_left_exact':str(self.common_left),
            'common_cut_original_M':M,'original_target_tail_sign_and_orientation_retained':True,
            'central_Q_regularization_included':False}
    def native_piece(self,cell):
        if cell in self.native_cache:return self.native_cache[cell]
        p=base.NativePiece(cell,self.raw,self.old)
        if cell>=self.common_start:
            n=3*self.M+2;lo=np.zeros((6,n),dtype=LD);hi=lo.copy();lo[:,0]=p.c.lo[:,0];hi[:,0]=p.c.hi[:,0];lo[:,-1]=p.c.lo[:,-1];hi[:,-1]=p.c.hi[:,-1]
            for axis in range(3):
                lo[:,axis*self.M+1:axis*self.M+self.oldM+1]=p.c.lo[:,axis*self.oldM+1:(axis+1)*self.oldM+1]
                hi[:,axis*self.M+1:axis*self.M+self.oldM+1]=p.c.hi[:,axis*self.oldM+1:(axis+1)*self.oldM+1]
            aa=(p.left-self.common_left)/self.common_width;bb=p.width/self.common_width;c=I(lo,hi)
            for j in range(6):
                v=I(0)
                for degree,cc in zip((3,4,5),self.common_poly):
                    if degree>=j:v=v+math.comb(degree,j)*aa**(degree-j)*bb**j*cc
                value=c[j]+v;c.lo[j]=value.lo;c.hi[j]=value.hi
            p.c=c;p.d=I(np.stack([(j*c[j]/p.width).lo for j in range(1,6)]),np.stack([(j*c[j]/p.width).hi for j in range(1,6)]));p.M=self.M
        self.native_cache[cell]=p;return p
    def native_batch(self,cells):
        parts=[self.native_piece(i) for i in cells]
        if len(set(p.M for p in parts))!=1:raise ValueError('Batch must split original common-cut support')
        obj=base.NativeBatch.__new__(base.NativeBatch);obj.cells=cells;obj.lefts=arrq([p.left for p in parts]);obj.widths=arrq([p.width for p in parts]);obj.M=parts[0].M
        obj.cc=I(np.stack([p.c.lo for p in parts],axis=1),np.stack([p.c.hi for p in parts],axis=1));obj.dd=I(np.stack([p.d.lo for p in parts],axis=1),np.stack([p.d.hi for p in parts],axis=1))
        return obj
