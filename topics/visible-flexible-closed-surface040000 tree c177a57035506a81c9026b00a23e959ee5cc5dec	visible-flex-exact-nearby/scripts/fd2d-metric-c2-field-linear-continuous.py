#!/usr/bin/env python3
"""Continuous linear metric residual of an ACTUAL saved C2 material field.

The prefix is compared with its own frozen target, in physical material
angle. All small numerators are formed as finite radial/Fourier polynomials
before bounds. Prefix angular denominators are bounded on complete arcs;
there is no angular sampling assertion. The physical radius derivative is
bounded analytically by one, without differentiating a packet remainder.

This supplies L=(X*e-g)+Lie_v(g), not a nonlinear pullback certificate.
The exact common-target transfer and nonlinear budget are separate inputs.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
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

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
sp=importlib.util.spec_from_file_location('fd2d_linear_field_bounds',HERE/'fd2d-metric-material-field-bounds.py')
fb=importlib.util.module_from_spec(sp);sys.modules[sp.name]=fb;sp.loader.exec_module(fb)
diff,I,qb,poly=fb.diff,fb.I,fb.qb,fb.poly
P=poly.P
_original_convolution=poly.interval_convolution


def small_factor_convolution(a,b):
    """Same interval product; use Toeplitz radial matrices for narrow factors."""
    if a.lo.shape[1]<b.lo.shape[1]:a,b=b,a
    if b.lo.shape[1]>7:return _original_convolution(a,b)
    if b.lo.shape==(1,1):return a*b[0,0]
    da,ma=a.lo.shape;db,mb=b.lo.shape;degree=da+db-1
    out=I(np.zeros((degree,ma+mb-1)))
    for angular in range(mb):
        lo=np.zeros((degree,da));hi=lo.copy()
        for j in range(da):lo[j:j+db,j]=b.lo[:,angular];hi[j:j+db,j]=b.hi[:,angular]
        product=poly.interval_matmul(I(lo,hi),a)
        value=out[:,angular:angular+ma]+product
        out.lo[:,angular:angular+ma]=value.lo;out.hi[:,angular:angular+ma]=value.hi
    return out


poly.interval_convolution=small_factor_convolution


def restrict(c,a,b):
    """Exact rational affine coefficients, then outward polynomial sums."""
    out=[];degree=c.lo.shape[0]-1
    for k in range(degree+1):
        value=I(np.zeros(c.lo.shape[1]))
        for j in range(k,degree+1):
            weight=Q(math.comb(j,k))*a**(j-k)*b**k
            if weight:value=value+c[j]*qb(weight)
        out.append(value)
    return diff.base.stack(out,0)


def native_power(power,mesh,index,left,right,derivative):
    h=mesh[index+1]-mesh[index];a=(left-mesh[index])/h;b=(right-left)/h
    if not 0<=a<a+b<=1:raise ValueError('Restriction crosses a defining knot')
    raw=power[derivative:]
    factors=np.array([math.factorial(k)//math.factorial(k-derivative) for k in range(derivative,6)])[:,None]
    raw=raw*factors*qb(Q(1)/h**derivative)
    return restrict(raw,a,b)


def scalar_real_polynomials(cosine,sine):
    degree,m=cosine.lo.shape;M=m-1
    lo=np.zeros((degree,2*M+1));hi=lo.copy()
    lo[:,M]=cosine.lo[:,0];hi[:,M]=cosine.hi[:,0]
    if M:
        half=cosine[:,1:]/2
        lo[:,M+1:]=half.lo;hi[:,M+1:]=half.hi
        lo[:,:M]=half.lo[:,::-1];hi[:,:M]=half.hi[:,::-1]
    even=P(I(lo,hi),-M,0)
    lo=np.zeros_like(lo);hi=lo.copy()
    if M:
        half=sine[:,1:]/2
        lo[:,:M]=half.lo[:,::-1];hi[:,:M]=half.hi[:,::-1]
        lo[:,M+1:]=-half.hi;hi[:,M+1:]=-half.lo
    return even,P(I(lo,hi),-M,1)


class Field:
    def __init__(self,path):
        self.path=path;self.meta,self.x,self.jets,self.bindings=fb.read_field(path)
        self.mesh=[Q(float(x)) for x in self.x];self.M=self.meta['modes'];self.cache={}

    def fields(self,left,right):
        i=min(bisect.bisect_right(self.mesh,left)-1,len(self.mesh)-2)
        if i<0:raise ValueError('Field point precedes defined interval')
        if i not in self.cache:
            c,_,_=fb.powers(self.jets,self.x,i,i+1)
            self.cache={i:I(c.lo[0].reshape(6,-1),c.hi[0].reshape(6,-1))}
        raw=self.cache[i];out=[]
        for d in range(2):
            c=native_power(raw,self.mesh,i,left,right,d);degree=c.lo.shape[0]
            c=I(c.lo.reshape(degree,2,self.M+1,2),c.hi.reshape(degree,2,self.M+1,2))
            out.append([scalar_real_polynomials(c[:,j,:,0],c[:,j,:,1]) for j in range(2)])
        return out


class Warp:
    def __init__(self,meta,target):
        self.source=diff.module('fd2d_linear_warp_supplier',HERE/'78718-prefix-metric-supplier-storage-v1.py')
        self.knots,self.coeff=self.source.exact_clamped_spline(meta['chart'])
        self.end=Q(target['frozen_total_end']);self.amplitude=8*Q(float(meta['warp_reference_q']))
        self.cuts=[x*self.end for x in sorted(set(self.knots+[Q(3,4)]))]

    def coefficients(self,left,right):
        x=left/self.end;width=(right-left)/self.end
        j=min(bisect.bisect_right(self.knots,x)-1,len(self.coeff)-1)
        c=self.source.compose(self.coeff[j],[x-self.knots[j],width])
        if x>=Q(3,4):
            cutoff=self.source.compose([Q(1),Q(0),Q(0),Q(-10),Q(15),Q(-6)],[(x-Q(3,4))*4,width*4])
            c=self.source.mul(c,cutoff)
        c=self.source.scale(c,self.amplitude);d=self.source.scale(self.source.der(c),1/(right-left))
        def pack(v):
            q=[qb(x) for x in v]
            return P(I(np.array([x.lo for x in q])[:,None],np.array([x.hi for x in q])[:,None]))
        return pack(c),pack(d)


def real_coefficients(p):
    degree,width=p.c.lo.shape;last=p.first+width-1;M=max(abs(p.first),abs(last))
    lo=np.zeros((degree,2*M+1));hi=lo.copy();offset=p.first+M
    lo[:,offset:offset+width]=p.c.lo;hi[:,offset:offset+width]=p.c.hi;c=I(lo,hi)
    zero=c[:,M:M+1] if p.phase==0 else I(np.zeros((degree,1)))
    negative=c[:,:M][:,::-1];positive=c[:,M+1:]
    rest=negative+positive if p.phase==0 else negative-positive
    return I(np.concatenate((zero.lo,rest.lo),axis=1),np.concatenate((zero.hi,rest.hi),axis=1))


def coefficient_ranges(p):
    c=real_coefficients(p);b=poly.interval_matmul(poly.bernstein_matrix(c.lo.shape[0]-1),c)
    return I(b.lo.min(axis=0)[None,:],b.hi.max(axis=0)[None,:])


_trig={}


def trigonometry(modes,count):
    key=(modes,count)
    if key in _trig:return _trig[key]
    # Every endpoint is a count-th root; reduce before the exact Taylor cache.
    cp=[diff.base.trig_point(Q(2*k,count),True) for k in range(count)]
    sn=[diff.base.trig_point(Q(2*k,count),False) for k in range(count)]
    cl=np.ones((modes+1,count));ch=cl.copy();sl=cl.copy();sh=cl.copy()
    def ceil_div(a,b):return -((-a)//b)
    for j in range(1,modes+1):
        if j>=count:cl[j]=-1;ch[j]=1;sl[j]=-1;sh[j]=1;continue
        for k in range(count):
            a,b=(j*k)%count,(j*(k+1))%count
            cl[j,k]=min(cp[a][0],cp[b][0]);ch[j,k]=max(cp[a][1],cp[b][1])
            sl[j,k]=min(sn[a][0],sn[b][0]);sh[j,k]=max(sn[a][1],sn[b][1])
            left,right=j*k,j*(k+1)
            if ceil_div(left,count)<=right//count:ch[j,k]=1
            if ceil_div(2*left-count,2*count)<=(2*right-count)//(2*count):cl[j,k]=-1
            if ceil_div(4*left-count,4*count)<=(4*right-count)//(4*count):sh[j,k]=1
            if ceil_div(4*left-3*count,4*count)<=(4*right-3*count)//(4*count):sl[j,k]=-1
    _trig[key]=(I(cl,ch),I(sl,sh));return _trig[key]


def range_poly(p,trig=None):
    c=coefficient_ranges(p)
    if trig is None:
        if c.lo.shape[1]!=1:raise ValueError('Expected scalar polynomial')
        return c[0,0]
    table=trig[p.phase][:c.lo.shape[1]]
    result=poly.interval_matmul(c,table)
    return result[0]


def matrix_norm(a,b,c):
    aa,bb,cc=a.abs().hi,b.abs().hi,c.abs().hi
    g=np.maximum((I(aa)+I(bb)).hi,(I(bb)+I(cc)).hi)
    disc=(a-c).square()+4*b.square();disc=I(np.maximum(0,disc.lo),disc.hi)
    exact=((a+c).abs()+disc.sqrt())/2
    return float(np.min(np.array([float(np.max(g)),float(np.max(exact.hi))])))


def expand_geometry(v,modes):
    degree=v.lo.shape[0];zero=I(np.zeros((degree,modes+1)))
    def join(a,b):return I(np.concatenate((a.lo,b.lo),axis=1),np.concatenate((a.hi,b.hi),axis=1))
    r=join(v[:,0:1],v[:,1:modes+1]);t=join(I(np.zeros((degree,1))),v[:,modes+1:2*modes+1])
    z=join(v[:,-1:],v[:,2*modes+1:3*modes+1])
    return scalar_real_polynomials(r,zero)[0],scalar_real_polynomials(zero,t)[1],scalar_real_polynomials(z,zero)[0]


class Prefix:
    def __init__(self,geometry,target,field):
        self.geometry_path=geometry;self.target_path=target;self.field=field
        self.geom,self.bindings=diff.load_geometry(geometry,'linear_actual_prefix')
        self.meta=json.loads(geometry.read_text());self.target=json.loads(target.read_text())
        basehash=self.meta.get('base_geometry_sha256',diff.identity(geometry)['sha256'])
        if self.target['geometry_sha256']!=basehash:raise ValueError('Wrong own target for common prefix')
        data=target.parent/self.target['data_file'];payload=data.read_bytes()
        if hashlib.sha256(payload).hexdigest()!=self.target['data_sha256']:raise ValueError('Changed target packet')
        with np.load(io.BytesIO(gzip.decompress(payload)),allow_pickle=False) as raw:self.data={k:raw[k].copy() for k in raw.files}
        self.target_data=diff.identity(data);self.left=list(map(lambda x:Q(float(x)),self.data['left']))
        self.right=list(map(lambda x:Q(float(x)),self.data['right']))
        if self.left[0]!=0 or self.right[-1]!=self.geom.exact_length or self.right[:-1]!=self.left[1:]:
            raise ValueError('Target does not cover the actual prefix')
        self.warp=Warp(self.meta,self.target)
        self.mesh=sorted(set(self.geom.exact_mesh+self.left+self.right+self.field.mesh+self.warp.cuts))
        if self.field.mesh[0]!=0 or self.field.mesh[-1]!=self.geom.exact_length:raise ValueError('Field has a different prefix domain')
        self.cosine=P(I(np.array([[.5,0,.5]])),-1,0);self.sine=P(I(np.array([[.5,0,-.5]])),-1,1)

    def polynomials(self,left,right):
        i=min(bisect.bisect_right(self.geom.exact_mesh,left)-1,len(self.geom.x)-2)
        val,der=[native_power(self.geom.power[i],self.geom.exact_mesh,i,left,right,d) for d in range(2)]
        r,t,z=expand_geometry(val,self.geom.M);rs,ts,zs=expand_geometry(der,self.geom.M)
        rp,tp,zp=r.theta()-t,r+t.theta(),z.theta()
        E=rs*rs+ts*ts+zs*zs;F=rs*rp+ts*tp+zs*zp;G=rp*rp+tp*tp+zp*zp
        j=min(bisect.bisect_right(self.left,left)-1,len(self.left)-1)
        if right>self.right[j]:raise ValueError('A linear interval crosses its target packet')
        A0=poly.target_scalar(self.data,'a',j)
        A=P(restrict(A0.c,(left-self.left[j])/(self.right[j]-self.left[j]),
                     (right-left)/(self.right[j]-self.left[j])))
        e,ep=self.warp.coefficients(left,right);rho=P.scalar(1.)-e*self.cosine;nu=ep*self.sine*qb(Q(-1,3));a2=A*A
        D=E-(1+a2*nu*nu);B=F-a2*nu*rho;N=G-a2*rho*rho
        field=self.field.fields(left,right);(pe,po),(qe,qo)=field[0];(pse,pso),(qse,qso)=field[1]
        rr=rho*rho*D-2*nu*rho*B+nu*nu*N+2*rho*rho*pse-2*nu*rho*pe.theta()
        rr_noise=2*rho*rho*pso-2*nu*rho*po.theta()
        rt=rho*B-nu*N+rho*pe.theta()+a2*rho*rho*qso-a2*nu*rho*qo.theta()
        rt_noise=rho*po.theta()+a2*rho*rho*qse-a2*nu*rho*qe.theta()
        tt=N+2*a2*rho*qo.theta();tt_noise=2*a2*rho*qe.theta()
        return dict(main=(rr,rt,tt),noise=(rr_noise,rt_noise,tt_noise),A=A,e=e,rho=rho,p=(pe,po))

    def bound(self,left,right,angular):
        data=self.polynomials(left,right);A=range_poly(data['A']);e=range_poly(data['e'])
        if A.lo<=0 or float(e.abs().hi)>=1:raise ValueError('Target scalar positivity failed')
        max_mode=max(max(abs(p.first),abs(p.first+p.c.lo.shape[1]-1)) for p in (*data['main'],*data['noise'],*data['p']))
        trig=trigonometry(max_mode,angular)
        rho=1-e*trig[0][1]
        if np.any(rho.lo<=0):raise ValueError('Arc material chart positivity failed')
        values=[range_poly(p,trig)+range_poly(q,trig) for p,q in zip(data['main'],data['noise'])]
        # The exact frozen profile has |a_s|<=1 (flat ramp speeds<1, bridge is sine).
        # Keep this small radial term separate so its rho^2 cancels exactly.
        pvalue=range_poly(data['p'][0],trig)+range_poly(data['p'][1],trig)
        b0=values[0]/rho.square();b1=values[1]/(A*rho.square())
        b2=values[2]/(A.square()*rho.square())+I(-1.,1.)*2*pvalue/A
        return matrix_norm(b0,b1,b2)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry',type=Path,required=True);p.add_argument('--target',type=Path,required=True)
    p.add_argument('--field',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--rows',type=Path);p.add_argument('--start',type=int,default=0);p.add_argument('--stop',type=int)
    p.add_argument('--angular',type=int,default=256);p.add_argument('--threshold',type=float,default=1.9e-9)
    p.add_argument('--radial-subdivisions',type=int,default=1);args=p.parse_args();started=time.monotonic()
    if args.out.exists() or (args.rows is not None and args.rows.exists()):raise FileExistsError('Use new reports')
    field=Field(args.field)
    if field.meta['region']!='prefix':raise ValueError('This entry point currently requires a prefix field')
    model=Prefix(args.geometry,args.target,field);total=len(model.mesh)-1
    stop=total if args.stop is None else min(total,args.stop)
    if not 0<=args.start<stop:raise ValueError('Invalid selected range')
    maximum=0.;worst=None;rows=[]
    for cell in range(args.start,stop):
        a,b=model.mesh[cell:cell+2]
        for sub in range(args.radial_subdivisions):
            left=a+(b-a)*Q(sub,args.radial_subdivisions);right=a+(b-a)*Q(sub+1,args.radial_subdivisions)
            bound=model.bound(left,right,args.angular)
            row=dict(cell=cell,subdivision=sub,left_exact=str(left),right_exact=str(right),linear_operator_upper=bound)
            if bound>maximum:maximum=bound;worst=row
            if args.rows is not None:rows.append(row)
        if (cell-args.start+1)%100==0:print(json.dumps(dict(cells=cell-args.start+1,total=stop-args.start,
            maximum=maximum,seconds=time.monotonic()-started)),flush=True)
    complete=args.start==0 and stop==total
    report=dict(schema='fd2d-continuous-prefix-linear-material-residual-v1',scope=__doc__,script=diff.identity(__file__),
        geometry=diff.identity(args.geometry),target=diff.identity(args.target),target_data=model.target_data,
        field=diff.identity(args.field),field_bindings=field.bindings,geometry_bindings=model.bindings,
        total_radial_cells=total,selected_radial_cells=stop-args.start,radial_subdivisions=args.radial_subdivisions,
        angular_arcs_covering_one_threefold_period=args.angular,all_finite_angular_modes_covered=True,
        complete_prefix_domain=complete,linear_operator_upper=maximum,worst_interval=worst,
        threshold=args.threshold,threshold_met=complete and maximum<=args.threshold,
        target_kind='own frozen analytic metric; exact common bridge transfer is separate',
        physical_radius_derivative_bound=1.,nonlinear_pullback_certified=False,whole_surface_certified=False,
        seconds=time.monotonic()-started)
    if args.rows is not None:
        if args.rows.suffix!='.gz':raise ValueError('Use gzip rows')
        payload=gzip.compress((json.dumps(rows,separators=(',',':'))+'\n').encode(),mtime=0)
        if len(payload)>=5_000_000:raise ValueError('Too many row bytes')
        args.rows.write_bytes(payload);report['row_data']=diff.identity(args.rows)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out),linear_operator_upper=maximum,complete=complete,
                         threshold_met=report['threshold_met'],seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
