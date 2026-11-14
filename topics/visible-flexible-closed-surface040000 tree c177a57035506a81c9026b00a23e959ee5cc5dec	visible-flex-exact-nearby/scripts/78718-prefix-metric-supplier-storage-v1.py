#!/usr/bin/env python3
# New 78718 explicit storage adaptation; original mathematical source is retained below.
"""Analytic target packets for a flat-ramp prefix plus a sine-integral bridge.

The main prefix parameters are exact binary rationals; Tu/Td are recomputed
as exact rational expressions. The angular clamped cubic spline is solved
over Fraction, not rounded PPoly coefficients. The bridge uses frozen
binary L,pt,ps, but its sine integral is certified by Taylor bounds. This
does NOT certify that those bridge constants are the exact matching root.
The endpoint radius/derivative discrepancies are reported separately.
"""
import argparse
import bisect
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
sys.dont_write_bytecode=True

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('metric_backend',HERE/'78718-prefix-metric-polynomial-storage-v1.py')
backend=importlib.util.module_from_spec(spec);sys.modules[spec.name]=backend;spec.loader.exec_module(backend)
I,up,down,qbounds=backend.I,backend.up,backend.down,backend.qbounds


def q(x):return Q.from_float(float(x))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):
    z=[Q(0)]*max(len(a),len(b))
    for j,v in enumerate(a):z[j]+=v
    for j,v in enumerate(b):z[j]+=v
    return trim(z)
def scale(a,c):return [v*c for v in a]
def mul(a,b):
    z=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return trim(z)
def compose(a,b):
    z=[Q(0)]
    for x in a[::-1]:z=add(mul(z,b),[x])
    return z
def der(a):return [j*x for j,x in enumerate(a)][1:] or [Q(0)]
def polynomial_bound(a,lo,hi):return sum(map(abs,compose(a,[lo,hi-lo])),Q(0))
def qinterval(a,size):
    outlo=np.zeros(size);outhi=np.zeros(size)
    assert len(a)<=size
    for i,x in enumerate(a):
        z=qbounds(x);outlo[i]=z.lo;outhi[i]=z.hi
    return I(outlo,outhi)
def interval_add_poly(a,b):
    n=max(len(a.lo),len(b.lo));la=np.zeros(n);ha=la.copy();lb=la.copy();hb=la.copy()
    la[:len(a.lo)]=a.lo;ha[:len(a.hi)]=a.hi;lb[:len(b.lo)]=b.lo;hb[:len(b.hi)]=b.hi
    return I(la,ha)+I(lb,hb)
def interval_mul_poly(a,b):
    z=backend.interval_convolution(I(a.lo[:,None],a.hi[:,None]),I(b.lo[:,None],b.hi[:,None]))
    return I(z.lo[:,0],z.hi[:,0])


def exact_clamped_spline(chart):
    x=list(map(q,chart['knots']));y=list(map(q,chart['values']));n=len(x)
    if n<2 or len(y)!=n or x[0]!=0 or x[-1]!=1 or any(x[j+1]<=x[j] for j in range(n-1)):
        raise ValueError('Invalid exact spline knots')
    h=[x[j+1]-x[j] for j in range(n-1)]
    lower=[Q(0)]*n;diagonal=[Q(0)]*n;upper=[Q(0)]*n;rhs=[Q(0)]*n
    diagonal[0]=2*h[0];upper[0]=h[0];rhs[0]=6*(y[1]-y[0])/h[0]
    lower[-1]=h[-1];diagonal[-1]=2*h[-1];rhs[-1]=6*(q(chart['final_derivative'])-(y[-1]-y[-2])/h[-1])
    for j in range(1,n-1):
        lower[j]=h[j-1];diagonal[j]=2*(h[j-1]+h[j]);upper[j]=h[j]
        rhs[j]=6*((y[j+1]-y[j])/h[j]-(y[j]-y[j-1])/h[j-1])
    for j in range(1,n):
        factor=lower[j]/diagonal[j-1]
        diagonal[j]-=factor*upper[j-1];rhs[j]-=factor*rhs[j-1]
    z=[Q(0)]*n;z[-1]=rhs[-1]/diagonal[-1]
    for j in range(n-2,-1,-1):z[j]=(rhs[j]-upper[j]*z[j+1])/diagonal[j]
    coefficients=[]
    for j in range(n-1):
        slope=(y[j+1]-y[j])/h[j]-h[j]*(2*z[j]+z[j+1])/6
        coefficients.append([y[j],slope,z[j]/2,(z[j+1]-z[j])/(6*h[j])])
    return x,coefficients


class Target:
    def __init__(self,meta,port,source_root):
        cfg=meta['frozen_profile'];self.cfg=cfg
        if cfg.get('ramp_law')!='flat':raise ValueError('This supplier requires the flat ramp law')
        self.delta,self.vu,self.vd,self.eps=map(q,(cfg['delta'],cfg['vu'],cfg['vd'],cfg['ramp']))
        self.eta=q(cfg.get('ramp_eta',.1));self.sign=1 if cfg['direction']=='outward' else -1
        if not (self.delta>0 and 0<self.vu<1 and 0<self.vd<1 and 0<self.eps<Q(1,2) and 0<self.eta<Q(1,2)):
            raise ValueError('Flat-ramp parameter hypotheses fail')
        if cfg['direction'] not in ('outward','inward') or int(cfg['cycles'])!=cfg['cycles'] or cfg['cycles']<1:
            raise ValueError('Invalid cycle data')
        self.Tu=self.delta/(self.vu*(1-self.eps));self.Td=self.delta/(self.vd*(1-self.eps))
        self.period=self.Tu+self.Td;self.prefix_end=self.period*int(cfg['cycles'])
        self.first,self.second=(self.Tu,self.Td) if self.sign==1 else (self.Td,self.Tu)
        # Only this extraction uses the original helper; no original a(s)
        # or quadrature value is used as a target enclosure.
        sys.path.insert(0,str(source_root/'topics/large-amplitude-twist-flex/scripts'))
        from f6curve_bidirectional_bridge import DirectionalBridge
        bridge=DirectionalBridge(port['cut'])
        self.bridge_source_sha256=sha(source_root/'topics/large-amplitude-twist-flex/scripts/f6curve_bidirectional_bridge.py')
        self.L,self.pt,self.ps=map(q,(bridge.L,bridge.pt,bridge.ps));self.sigma=int(bridge.sigma)
        self.end=q(meta['end'])
        self.bridge_constants={k:str(v) for k,v in [('L',self.L),('pt',self.pt),('ps',self.ps)]}
        self.bridge_constants['root_status']='Frozen numeric constants only; exact matching root not certified.'
        self.spline_x,self.spline_c=exact_clamped_spline(meta['chart'])
        self.warp=8*q(meta['warp_reference_q'])
        self.a_pieces=[]
        e,h=self.eps,self.eta
        us=[Q(0),e*h,e*(1-h),e,1-e,1-e+e*h,1-e*h,Q(1)]
        for cycle in range(int(cfg['cycles'])):
            for phase,T,start in [(0,self.first,cycle*self.period),(1,self.second,cycle*self.period+self.first)]:
                for k in range(len(us)-1):self.a_pieces.append((start+T*us[k],start+T*us[k+1],(phase,T,start,k)))
        self.a_starts=[p[0] for p in self.a_pieces]
        e_breaks=sorted(set(self.spline_x+[Q(3,4)]))
        self.e_pieces=[]
        for l,r in zip(e_breaks[:-1],e_breaks[1:]):
            mid=(l+r)/2;j=min(bisect.bisect_right(self.spline_x,mid)-1,len(self.spline_c)-1)
            self.e_pieces.append((l*self.end,r*self.end,(j,mid>=Q(3,4))))
        self.e_starts=[p[0] for p in self.e_pieces]
        self.anchor=None;self.anchor_location=None
        self.max_prefix_piece_extension=Q(0);self.max_chart_piece_extension=Q(0)
        self.max_prefix_bridge_wrong_side_sliver=Q(0)
        self.prefix_bridge_extension_allowance=self.eps*self.eta*self.second/4

    def a_prefix_poly(self,left,right,info):
        phase,T,start,k=info;e,h=self.eps,self.eta
        u=[(left-start)/T,(right-left)/T]
        if k==3:integral=add(u,[-e/2])
        else:
            t=scale(u,1/e) if k<3 else scale(add([1],scale(u,-1)),1/e)
            low=[Q(0),Q(0),Q(0),Q(0),1/(4*h*h*(1-h)),-1/(10*h**3*(1-h))]
            # This polynomial belongs to the specified analytic piece even
            # when the audit span overlaps a neighbouring exact breakpoint.
            # Choosing by the audit midpoint again would erase the alternate
            # branch needed to enclose that tiny overlapping part.
            branch=k if k<3 else 6-k
            if branch==0:primitive=compose(low,t)
            elif branch==2:primitive=add(add(t,[-Q(1,2)]),compose(low,add([1],scale(t,-1))))
            elif branch==1:primitive=compose([3*h*h/(20*(1-h)),-h/(2*(1-h)),1/(2*(1-h))],t)
            else:raise ValueError('Invalid flat-ramp analytic piece')
            integral=scale(primitive,e) if k<3 else add([1-e],scale(primitive,-e))
        amp=self.sign*self.delta/(1-e)
        return add([1 if phase==0 else 1+self.sign*self.delta],scale(integral,amp if phase==0 else -amp))

    def e_poly(self,left,right,info):
        j,cut=info;x=[left/self.end,(right-left)/self.end]
        z=compose(self.spline_c[j],add(x,[-self.spline_x[j]]))
        if cut:
            t=scale(add(x,[-Q(3,4)]),4)
            cutoff=compose([1,0,0,-10,15,-6],t)
            z=mul(z,cutoff)
        return scale(z,self.warp)

    def chart_packet(self,left,right):
        mid=(left+right)/2;j=min(bisect.bisect_right(self.e_starts,mid)-1,len(self.e_pieces)-1)
        primary=self.e_poly(left,right,self.e_pieces[j][2]);primary_der=scale(der(primary),1/(right-left))
        ev,ed=Q(0),Q(0)
        first=max(0,bisect.bisect_right(self.e_starts,left)-1)
        last=min(len(self.e_pieces),bisect.bisect_left(self.e_starts,right)+1)
        for k in range(first,last):
            l,r,info=self.e_pieces[k];l=max(left,l);r=min(right,r)
            if l>=r or k==j:continue
            alt=self.e_poly(left,right,info);alt_der=scale(der(alt),1/(right-left))
            u,v=(l-left)/(right-left),(r-left)/(right-left)
            ev=max(ev,polynomial_bound(add(alt,scale(primary,-1)),u,v))
            ed=max(ed,polynomial_bound(add(alt_der,scale(primary_der,-1)),u,v))
        self.max_chart_piece_extension=max(self.max_chart_piece_extension,ev,ed)
        return qinterval(primary,9),qinterval(primary_der,8),float(qbounds(ev).hi),float(qbounds(ed).hi)

    @staticmethod
    def sincos(x):
        xi=qbounds(x);s=I(0.);c=I(0.);power=I(1.)
        for k in range(26):
            if k%2:s=s+power*qbounds(Q((-1)**((k-1)//2),math.factorial(k)))
            else:c=c+power*qbounds(Q((-1)**(k//2),math.factorial(k)))
            power=power*xi
        mag=I(max(abs(float(xi.lo)),abs(float(xi.hi))))
        error=I(1.)
        for _ in range(26):error=error*mag
        error=error*qbounds(Q(1,math.factorial(26)))
        return s+I(-float(error.hi),float(error.hi)),c+I(-float(error.hi),float(error.hi))

    def bridge_packet(self,left,right):
        ds=right-left
        if self.anchor is None:
            gap=abs(left-self.prefix_end)
            if gap>Q(1,10**10):raise ValueError('First bridge interval is not adjacent to the exact prefix end')
            error=float(qbounds(gap).hi)
            self.anchor=I(float(down(1-error)),float(up(1+error)));self.anchor_location=left
        if self.anchor_location!=left:raise ValueError('Bridge intervals must be consecutive')
        t=[(left-self.prefix_end)/self.L,ds/self.L]
        phi=compose([0,0,3*self.pt-self.L*self.ps,-2*self.pt+self.L*self.ps],t)
        center=compose(phi,[Q(1,2)])[0]
        change=add(phi,[-center]);w=qinterval(change,4)
        sin,cos=self.sincos(center);derivatives=[sin,cos,-sin,-cos]
        power=I(np.array([1.]));poly=I(np.array([0.]))
        for k in range(6):
            poly=interval_add_poly(poly,power*derivatives[k%4]*qbounds(Q(1,math.factorial(k))))
            power=interval_mul_poly(power,w)
        W=backend.positive_sum_upper(np.maximum(abs(w.lo),abs(w.hi)))
        err=I(1.)
        for _ in range(6):err=err*I(W)
        err=err*qbounds(ds/Q(math.factorial(6)))
        coefflo=np.zeros(len(poly.lo)+1);coeffhi=coefflo.copy()
        coefflo[0]=self.anchor.lo;coeffhi[0]=self.anchor.hi
        for k in range(len(poly.lo)):
            c=poly[k]*qbounds(self.sigma*ds/Q(k+1));coefflo[k+1]=c.lo;coeffhi[k+1]=c.hi
        full=I(coefflo,coeffhi)
        anchor=I(0.)
        for k in range(len(full.lo)):anchor=anchor+full[k]
        anchor=anchor+I(-float(err.hi),float(err.hi))
        self.anchor,self.anchor_location=anchor,right
        trunc=backend.positive_sum_upper(np.maximum(abs(full.lo[9:]),abs(full.hi[9:])))
        extra=float(up(float(err.hi)+trunc))
        if left<self.prefix_end:extra=float(up(extra+float(qbounds(2*(self.prefix_end-left)).hi)))
        return I(full.lo[:9],full.hi[:9]),extra

    def radius_packet(self,left,right):
        mid=(left+right)/2
        if mid>=self.prefix_end:return self.bridge_packet(left,right)
        j=min(bisect.bisect_right(self.a_starts,mid)-1,len(self.a_pieces)-1)
        primary=self.a_prefix_poly(left,right,self.a_pieces[j][2]);err=Q(0)
        first=max(0,bisect.bisect_right(self.a_starts,left)-1)
        last=min(len(self.a_pieces),bisect.bisect_left(self.a_starts,right)+1)
        for k in range(first,last):
            l,r,info=self.a_pieces[k];l=max(left,l);r=min(right,r)
            if l>=r or k==j:continue
            alt=self.a_prefix_poly(left,right,info)
            err=max(err,polynomial_bound(add(alt,scale(primary,-1)),(l-left)/(right-left),(r-left)/(right-left)))
        if right>self.prefix_end:
            sliver=right-self.prefix_end
            # Outside the last flat-ramp piece the polynomial is an
            # extrapolation.  This guard gives |t/eta|<1/4, hence |P'(t)|<1
            # and the required speed bound for the two-Lipschitz difference.
            if not sliver<self.prefix_bridge_extension_allowance:
                raise ValueError('Prefix/bridge overlap exceeds the proven polynomial extension range')
            self.max_prefix_bridge_wrong_side_sliver=max(self.max_prefix_bridge_wrong_side_sliver,sliver)
            err=max(err,2*sliver)
        self.max_prefix_piece_extension=max(self.max_prefix_piece_extension,err)
        return qinterval(primary,9),float(qbounds(err).hi)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--geometry',type=Path,required=True);ap.add_argument('--source-root',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True);args=ap.parse_args()
    start=time.monotonic();geom=backend.base.ExactHermite(args.geometry);meta=dict(geom.meta)
    meta['end']=float(geom.x[-1]);port_path=Path(meta['linear_port'])
    if sha(port_path)!=meta['port_sha256']:raise ValueError('Frozen port hash mismatch')
    port=json.loads(port_path.read_text());target=Target(meta,port,args.source_root)
    breaks=[float(x) for x in target.a_starts]+[float(target.prefix_end)]+[float(x) for x in target.e_starts]
    x=np.unique(np.r_[geom.x,[v for v in breaks if geom.x[0]<v<geom.x[-1]]])
    n=len(x)-1
    data={'left':x[:-1],'right':x[1:]}
    for name,d in [('a',9),('e',9),('ep',8)]:
        data[name+'_lo']=np.zeros((n,d));data[name+'_hi']=np.zeros((n,d));data[name+'_remainder']=np.zeros(n)
    for k in range(n):
        left,right=q(x[k]),q(x[k+1]);a,ar=target.radius_packet(left,right);e,ep,er,epr=target.chart_packet(left,right)
        for name,val,err in [('a',a,ar),('e',e,er),('ep',ep,epr)]:
            data[name+'_lo'][k]=val.lo;data[name+'_hi'][k]=val.hi;data[name+'_remainder'][k]=err
    buf=io.BytesIO();np.savez(buf,**data)
    f=args.out_prefix.with_name(args.out_prefix.name+'-data.npz.gz');f.write_bytes(gzip.compress(buf.getvalue(),mtime=0))
    if f.stat().st_size>=5_000_000:raise ValueError('Data file exceeds repository size limit')
    terminal=target.anchor
    cut=q(port['cut']['radius'])
    value_gap=terminal-qbounds(cut)
    tt=(q(x[-1])-target.prefix_end)/target.L
    phi=compose([0,0,3*target.pt-target.L*target.ps,-2*target.pt+target.L*target.ps],[tt])[0]
    sin,cos=target.sincos(phi);derivative=sin*target.sigma
    derivative_target=q(port['cut'].get('radial_arclength_derivative',float(target.sigma/math.sqrt(port['cut']['E']))))
    derivative_gap=derivative-qbounds(derivative_target)
    output=dict(scope=__doc__,geometry_file=str(args.geometry),geometry_sha256=sha(args.geometry),
        geometry_storage_bindings=geom.storage_bindings,
        data_file=f.name,data_sha256=sha(f),script_sha256=sha(__file__),
        arithmetic_backend_sha256=sha(HERE/'78718-prefix-metric-polynomial-storage-v1.py'),
        frozen_profile=target.cfg,bridge_constants=target.bridge_constants,
        bridge_parameter_extractor_sha256=target.bridge_source_sha256,
        analytic_definition='Flat-ramp a(s): exact rational formulas in the saved binary main parameters; '
        'Tu,Td recomputed by Fraction. The clamped angular spline is solved exactly over Fraction and '
        'multiplied by the prescribed quintic cutoff. The bridge has frozen binary L,pt,ps but uses '
        'the true sine integral. Every bridge span uses a fifth-order Taylor enclosure around its '
        'exact midpoint phase, followed by integration and an explicitly bounded degree-eight truncation. '
        'The radius endpoint is not asserted to satisfy the exact bridge matching equation.',
        endpoint_radius_gap=[float(value_gap.lo),float(value_gap.hi)],
        endpoint_radial_arclength_derivative_gap=[float(derivative_gap.lo),float(derivative_gap.hi)],
        exact_prefix_end=str(target.prefix_end),frozen_total_end=str(q(x[-1])),
        frozen_bridge_endpoint_coordinate_gap=str(q(x[-1])-target.prefix_end-target.L),
        maximum_prefix_piece_extension_error=float(qbounds(target.max_prefix_piece_extension).hi),
        maximum_chart_piece_extension_error=float(qbounds(target.max_chart_piece_extension).hi),
        maximum_prefix_bridge_wrong_side_sliver=str(target.max_prefix_bridge_wrong_side_sliver),
        prefix_bridge_extension_allowance=str(target.prefix_bridge_extension_allowance),
        prefix_bridge_extension_guard_passed=True,
        maximum_remainder={k:float(data[k+'_remainder'].max()) for k in ('a','e','ep')},
        intervals=n,bytes=f.stat().st_size,seconds=time.monotonic()-start,
        exact_bridge_matching_root_certified=False,global_common_metric_assembly_certified=False,
        analytic_enclosure_status='Requires independent review of the supplier implementation and definition.')
    args.out_prefix.with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('scope','analytic_definition','frozen_profile')},indent=2))


if __name__=='__main__':main()
